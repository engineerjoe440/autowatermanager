# Barn Automation Hardware Interface
import threading
import time
import sys
import glob

try:
    from pijuice import PiJuice # Import pijuice module
    from RPLCD import CharLCD # Import Raspberry Pi LCD Controller
    import RPi.GPIO as GPIO # Import GPIO Controller
    GPIO.setwarnings(False) # Disable GPIO Warnings
    pijuice = PiJuice(1, 0x14) # Instantiate PiJuice interface object
except:
    print("Failed to import. Testing on Windows? Try on RPi!")
    time.sleep(5)
    sys.exit()

# Define Shared (Global) Variable
lcdmsg1 = ''
lcdmsg2 = ''

# Define LCD Shape
col = 24
row = 2
# Define LCD Pins
rs = 21
en = 23
d4 = 29
d5 = 35
d6 = 31
d7 = 33
# Define Relay Control GPIO Pins
RLY1 = 37
RLY2 = 38
RLY3 = 40
# Define Add'l GPIO Pins
gLED = 16
rLED = 19
gBTN = 13
rBTN = 11
phto = 12
# Define Add'l Parameters
start_time = 0.01

# Define Temperature Probe Parameters
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

# Define Functions Required to Read Ambient Temperature
def read_temp_raw():
    with open(device_file, 'r') as f:
        lines = f.readlines()
    return lines
def read_temp(scale='f'):
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        if scale.upper() == 'F':
            return( temp_f )
        elif scale.upper() == 'C':
            return( temp_c )
        else:
            return

# Define Hardware Control Class
class BarnHardware:
    def __init__(self):
        # Initialize LCD Display
        self.lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=col, rows=row,
                           pin_rs=rs, pin_e=en, pins_data=[d4,d5,d6,d7])
        time.sleep(start_time)
        self.lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=col, rows=row,
                           pin_rs=rs, pin_e=en, pins_data=[d4,d5,d6,d7])
        # Initialize Button and LED GPIO Pins
        GPIO.setup(gLED, GPIO.OUT, initial=0)
        GPIO.setup(rLED, GPIO.OUT, initial=0)
        GPIO.setup(RLY1, GPIO.OUT, initial=0)
        GPIO.setup(RLY2, GPIO.OUT, initial=0)
        GPIO.setup(RLY3, GPIO.OUT, initial=0)
        GPIO.setup(phto, GPIO.IN)
        GPIO.setup(gBTN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(rBTN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
    # Define Get Functions
    def get_btn(self):
        grn = GPIO.input(gBTN) == GPIO.HIGH
        red = GPIO.input(rBTN) == GPIO.HIGH
        return(grn,red)
    def get_photo(self):
        light = GPIO.input(phto) == GPIO.HIGH
        return(light)
    def get_lcd(self):
        global lcdmsg1, lcdmsg2
        return(lcdmsg1.replace('\0',' '),lcdmsg2.replace('\0',' '))
    def get_led(self):
        L1 = GPIO.input(gLED) == GPIO.HIGH
        L2 = GPIO.input(rLED) == GPIO.HIGH
    def get_rly(self):
        r1 = GPIO.input(RLY1) == GPIO.HIGH
        r2 = GPIO.input(RLY2) == GPIO.HIGH
        r3 = GPIO.input(RLY3) == GPIO.HIGH
        return(r1,r2,r3)
    def get_bat_sta(self):
        # Collect data structure and extract error
        sta = pijuice.status.GetStatus()['data']
        err = not( sta['error'] == 'NO_ERROR' )
        return(err)
    def get_bat_chg(self):
        chg = pijuice.status.GetChargeLevel()['data']
        return(chg) # percent charged
    def get_pwr_src(self):
        src = pijuice.status.GetStatus()['data']['powerInput']
        active = (src == 'PRESENT')
        return(active,src)
    def get_voltage(self):
        v = pijuice.status.GetBatteryVoltage()['data']
        return(float(v)*0.001)
    def get_current(self):
        i = pijuice.status.GetBatteryCurrent()['data']
        return(float(i))
    def get_vbus_5v(self):
        v = pijuice.status.GetIoVoltage()['data']
        return(float(v)*0.001)
    def get_ibus_5v(self):
        i = pijuice.status.GetIoCurrent()['data']
        return(float(i))
    def get_bat_led(self,LED):
        if isinstance(LED, int): # Condition Input
            LED = {1:'D1', 2:'D2', 3:'D3'}[LED]
        return(pijuice.status.GetLedState(LED)['data'])
    def get_temp(self,scale='f',fmt=None):
        # Mask Temperature Function for Ease
        temp = read_temp(scale=scale)
        if isinstance(fmt,str):
            temp = fmt.format(temp)
        return(temp)
    
    # Define Callback Specifiers
    def set_grn_callback(self,func,opt=GPIO.RISING):
        GPIO.add_event_detect(gBTN,opt,callback=func,bouncetime=100)
    def set_red_callback(self,func,opt=GPIO.RISING):
        GPIO.add_event_detect(rBTN,opt,callback=func,bouncetime=100)
    
    # Define Set Functions for LED's and LCD
    def set_led(self,grn=False,red=False):
        # Set LEDs
        GPIO.output(gLED,grn)
        GPIO.output(rLED,red)
    def set_bat_led(self,LED,r,g,b):
        if isinstance(LED, int): # Condition Input
            LED = {1:'D1', 2:'D2', 3:'D3'}[LED]
        pijuice.status.SetLedState(LED, [r,g,b])
    def set_rly(self,rly,status):
        # Define LUT
        rly = [RLY1,RLY2,RLY3][rly]
        # Set Relays
        GPIO.output(rly,status)
    def set_lcd(self,LINE1='',LINE2=''):
        global lcdmsg1, lcdmsg2
        NL = 16*' ' # 16 Spaces
        L2MX = 8
        # Condition and Test Inputs
        LINE1 = str(LINE1)
        LINE2 = str(LINE2)
        if len(LINE1) > col:
            print("WARNING: Line 1 is longer than "+str(col)+" characters.")
        if len(LINE2) > L2MX:
            print("WARNING: Line 2 is longer than "+str(L2MX)+" characters.")
        # Manage LCD Strings
        lcdmsg1 = '\r'+LINE1[:col].replace(' ','\0')
        lcdmsg2 = NL+LINE2[:L2MX].replace(' ','\0')
        # Update LCD
        if __name__ == '__main__':
            print("testing...",len(lcdmsg1),len(lcdmsg2))
        # Clear LCD
        self.lcd.clear()
        # Write Message
        self.lcd.write_string(lcdmsg2)
        self.lcd.write_string(lcdmsg1)

# Define Test Method
if __name__ == '__main__':
    try:
        print("Testing Script Operation...")
        print("Temperature:",read_temp(),"°F")
        hdw = BarnHardware()
        hdw.set_lcd("Outside Temperature:",str(round(read_temp(),2))+"'F")
        ctr = 0
        while(True):
            time.sleep(1)
            hdw.set_lcd("Outside Temperature:",str(round(read_temp(),2))+"'F")
            g,r = hdw.get_btn()
            hdw.set_led(g,r)
            print("Light:",hdw.get_photo(),"\tBat:",hdw.get_bat_chg(),"%")
            if ctr == 0:
                hdw.set_rly(0,False)
                hdw.set_rly(1,False)
                hdw.set_rly(2,False)
                ctr += 1
            elif ctr == 1:
                hdw.set_rly(0,True)
                ctr += 1
            elif ctr == 2:
                hdw.set_rly(1,True)
                ctr += 1
            elif ctr == 3:
                hdw.set_rly(2,True)
                ctr += 1
            else:
                ctr = 0
    finally:
        hdw.set_lcd('','')
        hdw.set_rly(False,False,False)
        time.sleep(0.5)
        GPIO.cleanup()

# END