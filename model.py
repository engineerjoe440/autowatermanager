# Water Temperature Model for AutoWaterManager
# (c) Stanley Solutions

# Import Required Libraries
import math as m
import configparser
from collections import OrderedDict

# Define Constants
k_full = 0.00513
k_half = 0.00276
shutoff = 35
turn_on = 33

# Define Conversion Functions
def gallons(liters):
    gal = liters/3.78541
    return(gal)
def liters(gallons):
    lit = gallons*3.78541
    return(lit)

# Start Configuration Parser Object
configfile = 'config.ini'
parser = configparser.ConfigParser()
parser.read(configfile)
# Load settings for system
for section in parser.sections():
    for setting, value in parser.items(section):
        exec( str(setting) + '="' + str(value) + '"' )

###################################################################################
# Define Single Trough (Unit) Temperature Model
class unit_model():
    def __init__(self,temp0,Pwatts,volume,k=k_full,
                 shutoff=shutoff,turn_on=turn_on,in_service='checked'):
        """
        unit_model
        
        Parameters
        ----------
        temp0:      float
                    Initial Temperature (degrees F)
        Pwatts:     float
                    Heater Element Rated Power in Watts
        volume:     float
                    Trough/Container Volume in Gallons
        k:          float, optional
                    Water Temperature Constant for Container,
                    defaults to 15-gallon full constant
        shutoff:    float, optional
                    Threshold to turn off heater (upper limit)
        turn_on:    float, optional
                    Threshold to turn on heater (lower limit)
        in_service: bool, optional
                    Control argument to enable or disable system.
        """
        # Define Simple Heater Internal Parameters
        # All Internal Parameters are Private, and Should be Hidden
        self._t0 = float(temp0)
        self._Pkw = float(Pwatts)*0.001
        self._k = k
        self._temp = float(temp0)
        self._heater_en = False
        self._threshold = float(shutoff)
        self._volume = float(volume)
        self._force_on = 0
        self._force_off = 0
        self._in_service = (in_service == 'checked')
        self._tactv = turn_on # Frezing, Activate Point
        # This Freezing (Activate Point) Specifys the Water Temperature
        # at which the model evaluates a required turn-on.
    
    def get_service(self):
        # Return Internal Service State
        return(self._in_service)
    
    def get_heater_state(self):
        # Return Internal Heater State
        return(self._heater_en)
    
    def get_temp(self):
        # Return Internal Temperature
        return(self._temp)
    
    def get_power(self):
        # Return Internal Heater Power Rating
        return(self._Pkw)
    
    def force(self,force_on=None,force_off=None):
        """
        unit_model.force
        
        Parameters
        ----------
        force_on:   int, optional
                    Control to force the heater on for a number of minutes.
        force_off:  int, optional
                    Control to force the heater off for a number of minutes.
        """
        # Accept Any External Configuration Controls
        if force_on != None:
            self._force_on = force_on
            self._force_off = 0
        elif force_off != None:
            self._force_off = force_off
            self._force_on = 0
    
    def update(self,ambient,EN=True):
        """
        unit_model.update
        
        Parameters
        ----------
        ambient:    float
                    Current ambient temperature.
        """
        # Temperature over Time Method, Models Heater and Cooling Params
        # Capture Most Recent Water Temperature
        temp = self._temp
        # Determine Temperature Change from Both Heating and Cooling
        newTemp = ambient + (temp-ambient)*m.exp(-self._k)
        heatC = (temp-32)*5/9 + (60*self._Pkw)/(4.2*liters(self._volume))
        heat = (heatC*9/5) + 32
        # Convert Heating Effect back to Fahrenheit
        dt_heat = heat-temp
        # Determine whether Heater should be Applied
        # (Temperature is Above Upper Limit and not Forced On) or Forced Off
        if ((temp >= self._threshold) and (self._force_on == 0)) or self._force_off:
            self._heater_en = False # Don't Heat
        # If System In Service and (Temp Below Threshold or Heater Already On) or Forced On
        elif (self._in_service and EN and ((temp <= self._tactv) or self._heater_en)) or self._force_on:
            self._heater_en = True # Apply Heater
            newTemp += dt_heat
        # Don't Heat By Default
        else:
            self._heater_en = False # Don't Heat
        # Decrement Force States if Any are Present
        if self._force_on:
            self._force_on -= 1
        if self._force_on:
            self._force_off -= 1
        # Store Temperature, Return Heater Status
        self._temp = newTemp
        return(self._heater_en)
    
    def cycle_baseline(self,lut_fmt=True,mintemp=22,maxtemp=31.9,units=12):
        # Method to Calculate the Baseline Number of Operating Cycles Allowed
        step_size = 0.1
        baseline = [] # Empty List to Begin
        basetemp = [] # Empty List to Begin
        # Load Internal Values
        Pkw = self._Pkw
        volume = self._volume
        temp_recovr = self._threshold
        temp_restart = self._tactv
        k = self._k
        ambient = mintemp
        # Iteratively Calculate Baseline Number of Cycles
        while ambient <= maxtemp:
            recovery = 0
            rest = 0
            temp_rest = temp_recovr
            temp_recv = ambient
            state = 2
            # Iteratively Process the Heating/Cooling Performance
            while state != 0:
                if temp_recv < temp_recovr:
                    heatC = (temp_recv-32)*5/9 + (60*Pkw)/(4.2*liters(volume))
                    heat = (heatC*9/5) + 32
                    dt_heat = heat-temp_recv
                    temp_recv = ambient + (temp_recv-ambient)*m.exp(-k) + dt_heat
                    recovery += 1
                    if not (temp_recv < temp_recovr):
                        state -= 1 # Indicate Completion of Test
                if temp_rest > temp_restart:
                    # Determine Temperature Change from Cooling
                    newTemp = ambient + (temp_rest-ambient)*m.exp(-k)
                    temp_rest = newTemp
                    rest += 1
                    if not (temp_rest > temp_restart):
                        state -= 1 # Indicate Completion of Test
            # Times have been Calculated, Store Baseline
            floor = m.floor(rest/recovery)
            if floor < 0:
                floor = 0
            elif floor > units:
                floor = units
            baseline.append(floor)
            basetemp.append(ambient)
            # Increment Ambient Temperature (Acting Index)
            ambient += step_size
        # Baseline has been fully Generated
        if lut_fmt:
            return(dict(zip([ '%.1f' % elem for elem in basetemp ],baseline)))
        return(basetemp,baseline)
    
    def baseline_const(self):
        baseline = self.cycle_baseline()
        for key,value in baseline.items():
            if value == 1:
                return(key)
###################################################################################


###################################################################################
# Define System Model For All Troughs and Heaters
class system_model():
    def __init__(self,ambient,shutoff=shutoff,t0=None):
        """
        system_model
        
        Parameters
        ----------
        ambient:    float
                    Ambient Temperature in degrees Fahrenheit
        shutoff:    float, optional
                    Thermal Shutoff point, default=35
        t0:         list of float, optional
                    Descriptive list containing all initial temperatures
                    in degrees Fahrenheit, default of None loads ambient
                    as the initial temp for all entries
        """
        if t0==None:
            t0 = [ambient]*13 # Use Ambient Temperature
        k = k_full
        self.shutoff = shutoff
        self.turn_on = turn_on
        self.basemintemp=22
        self.basemaxtemp=31.9
        self.num_units = 12
        # Start Configuration Parser Object
        configfile = 'config.ini'
        parser = configparser.ConfigParser()
        parser.read(configfile)
        # Load settings for system
        for section in parser.sections():
            for setting, value in parser.items(section):
                exec( "global " + str(setting) )
                exec( str(setting) + '="' + str(value) + '"' )
        # Instantiate Model for Each Trough
        self.H1A = unit_model(t0[0],power1a,size1a,k,self.shutoff,
                              self.turn_on,p1aserv)
        self.H1B = unit_model(t0[1],power1b,size1b,k,self.shutoff,
                              self.turn_on,p1bserv)
        self.H2A = unit_model(t0[2],power2a,size2a,k,self.shutoff,
                              self.turn_on,p2aserv)
        self.H2B = unit_model(t0[3],power2b,size2b,k,self.shutoff,
                              self.turn_on,p2bserv)
        self.H3A = unit_model(t0[4],power3a,size3a,k,self.shutoff,
                              self.turn_on,p3aserv)
        self.H3B = unit_model(t0[5],power3b,size3b,k,self.shutoff,
                              self.turn_on,p3bserv)
        self.H4A = unit_model(t0[6],power4a,size4a,k,self.shutoff,
                              self.turn_on,p4aserv)
        self.H4B = unit_model(t0[7],power4b,size4b,k,self.shutoff,
                              self.turn_on,p4bserv)
        self.H5A = unit_model(t0[8],power5a,size5a,k,self.shutoff,
                              self.turn_on,p5aserv)
        self.H5B = unit_model(t0[9],power5b,size5b,k,self.shutoff,
                              self.turn_on,p5bserv)
        self.H6A = unit_model(t0[10],power6a,size6a,k,self.shutoff,
                              self.turn_on,p6aserv)
        self.H6B = unit_model(t0[11],power6b,size6b,k,self.shutoff,
                              self.turn_on,p6bserv)
        self.STOCK = unit_model(t0[12],stockpower,sizestock,k,self.shutoff,
                                self.turn_on,stockserv)
        self.allmodels = [self.H1A,self.H1B,self.H2A,self.H2B,self.H3A,self.H3B,
                          self.H4A,self.H4B,self.H5A,self.H5B,self.H6A,self.H6B]
        # Remove Out-of-Service Heaters from List
        models = []
        for model in self.allmodels:
            if model.get_service():
                models.append(model)
        self.models = models
        # Determine the System Baseline
        base_const = 0
        # Iteratively Query the Baseline Constant from Each Model
        for model in self.models:
            const = float(model.baseline_const())
            if const > base_const:
                # New Baseline Determined
                base_const = const
                base_model = model
        # Generate New Look-Up Function Based on Baseline LUT
        self.base_lut = model.cycle_baseline(mintemp=self.basemintemp,
                                             maxtemp=self.basemaxtemp,
                                             units=self.num_units)
    
    def lookup_cycles(self,value):
        # Value: float; the current temperature
        # Simple Function to Evaluate How Many Control Cycles Allowable by Temp
        if value > self.basemaxtemp:
            cyc = -3
        elif value < self.basemintemp:
            cyc = 0
        else:
            value = '%.1f' % value
            cyc = self.base_lut[value]
        return(cyc+3)
    
    def update(self,ambient):
        """
        system_model.update
        
        Parameters
        ----------
        ambient:    float
                    Ambient air temperature in degrees Fahrenheit
        """
        if ambient < self.turn_on:
            # Determine Number of Cycles Allowed
            n_cycles = self.lookup_cycles(ambient)
            # Prioritize Troughs According to Current Temperature
            priorities = {}
            for model in self.models:
                # Add Dictionary Item with Temp as Key
                priorities[model.get_temp()] = model
            # Load Prioritized List
            priorities = dict(OrderedDict(sorted(priorities.items())))
            c_temps = list(priorities.keys())
            models = list(priorities.values()) # Extract Ordered List
            # Determine Number to Be Enabled
            if min(c_temps) > self.turn_on:
                # All Water Temperatures are Above Minimum Threshold
                n_contr = int(len(models)/(n_cycles))
                # Split into Active and Not Active Groups
                active = models[:n_contr]
                inactive = models[n_contr:]
                # Update Active Heaters
                for heater in active:
                    heater.update(ambient,EN=True)
                # Update Inactive Heaters
                for heater in inactive:
                    heater.update(ambient,EN=False)
            else:
                for heater in models:
                    heater.update(ambient,EN=True)
            # Manage Stock Tank
            # Stock Tank is Unregulated by Dispatch
            self.STOCK.update(ambient,EN=True)
        else:
            for heater in self.models:
                heater.update(ambient,EN=False)
            # Stock Tank is Unregulated by Dispatch
            self.STOCK.update(ambient,EN=False)
        # Return States of All Heaters
        return(self.get_state())
    
    def set_force(self,heater,state,time_set):
        """
        system_model.set_force
        
        Parameters
        ----------
        heater:     int
        state:      bool
        time_set:   float
        """
        # Extract Heater Model from List
        model = self.allmodels[heater]
        if state: # Turn On
            model.force(time_set,None)
        else:
            model.force(None,time_set)
    
    def get_state(self):
        # Iteratively Collect Heater States
        states = []
        for model in self.allmodels:
            states.append(model.get_heater_state())
        # Stock Tank is Unregulated by Dispatch
        states.append(self.STOCK.get_heater_state())
        return(states)
    
    def get_temp(self):
        # Iteratively Collect Water Temperatures
        temps = []
        for model in self.allmodels:
            temps.append(model.get_temp())
        temps.append(self.STOCK.get_temp()) # Stock Tank is Unregulated by Dispatch
        return(temps)
    
    def get_consumption(self):
        # Iteratively Collect Heater Power if Heater is Active
        p_tot = 0
        for model in self.models:
            if model.get_heater_state():
                p_tot += model.get_power()
        # Return Load in kWatts
        return(p_tot)
###################################################################################

# Define Built-In Test
if __name__ == '__main__':
    # Import Libraries
    import matplotlib.pyplot as plt
    # Define System Parameters
    ambient = 31
    system = system_model(ambient)
    water_temp = [[],[],[],[],[],[],[],[],[],[],[],[],[]]
    # Process twenty-four hours
    minutes = 60*24
    for i in range(minutes):
        # Update the Model Instances
        system.update(ambient)
        # Retrieve Water Temp
        temp = system.get_temp()
        # Split into Lists
        for ind,item in enumerate(temp):
            water_temp[ind].append(item)
    # Plot Temperatures Over Time
    plt.figure(figsize=(14, 8))
    for i,temp in enumerate(water_temp):
        if i < 12:
            plt.plot(temp,label='water temp '+str(i+1))
        else:
            plt.plot(temp,linestyle=':',label='stock water temp')
    plt.axhline(32)
    plt.xlabel('Time (minutes)')
    plt.ylabel('Temperature (°F)')
    plt.title("Water Tank System Monitor")
    plt.show()

###################################################################################
# Define Additional Formulas 
def min_maintain(volume,Pwatts,temp_maint=None,k=k_full):
    # Minimum Maintainable Temperature Method; Determines Minimum Ambient
    # Temperature to Maintain (at least) the Maintenence Temperature
    temp = turn_on # Freezing Point
    Pkw = Pwatts*0.001
    if temp_maint != None:
        temp = temp_maint
    # Iteratively Process Temperatures between -10 and 32
    for ambient in range(-10,32):
        # Determine Temperature Change from Both Heating and Cooling
        dcool = temp - (ambient + (temp-ambient)*m.exp(-k))
        heatC = (temp-32)*5/9 + (60*Pkw)/(4.2*liters(volume))
        heat = (heatC*9/5) + 32
        dheat = heat-temp
        if dheat >= dcool:
            mintemp = ambient
            return(mintemp)

def time_to_recover(ambient,volume,Pwatts,temp_recovr=None,t0=None,k=k_full):
    # Time to Recover Method; Determines the Time (in minutes) required
    # to Heat the Modeled Trough from Ambient to the Recovery Threshold
    time = 0
    Pkw = Pwatts*0.001
    if t0 == None:
        temp = ambient
    else:
        temp = t0
    if temp_recovr == None:
        temp_recovr = turn_on
    # Iteratively Process the Heating/Cooling Performance to Determine
    # the Time Required; Return -1 if more than 24 Hours Required
    while temp < temp_recovr:
        heatC = (temp-32)*5/9 + (60*Pkw)/(4.2*liters(volume))
        heat = (heatC*9/5) + 32
        dt_heat = heat-temp
        temp = ambient + (temp-ambient)*m.exp(-k) + dt_heat
        time += 1
        if time > 1440:
            return(-1) # Return in Error
    return(time)

def rest_time(ambient,t0,temp_restart=turn_on,k=k_full):
    # Determine the Allowable Resting Time Before a Heater Restart is Required
    time = 0
    temp = t0
    # Iteratively Calculate New Temperature and Count Time (in minutes)
    # If Time is Greater than 24 Hours, Return -1
    while temp > temp_restart:
        # Determine Temperature Change from Both Heating and Cooling
        newTemp = ambient + (temp-ambient)*m.exp(-k)
        temp = newTemp
        time += 1
        if time > 1440:
            return(-1) # Indicate Greater than 24 Hours Cool
    return(time)
###################################################################################

# END