####################################################################################
#  AutoWaterManager Main Operating Web Server
#  (c) Stanley Solutions
#  Joe Stanley - engineerjoe440@yahoo.com
####################################################################################

# Define Parameters
hostname = '0.0.0.0'
port = 80
lightRelay = 2 # 0-indexed

# Define Static Parameters
index_page = 'index.tpl'
settings_page = 'settings.tpl'

# Import Dependencies
import os
import time
import git
import csv
from bottle import route, run, template, static_file, error
from bottle import request, redirect, Bottle, auth_basic, abort
import configparser
import outletoperate as outlet
from datetime import datetime
from model import unit_model, system_model
import pam # Authentication Engine
from barnhardware import BarnHardware
from mailmanager import send_email, emailtemplate
from threader import RepeatedThread, OsCommand, CallThread

# Instantiate Objects
Webapp = Bottle()
hardware = BarnHardware()
model = system_model(hardware.get_temp())

# Indicate Boot on LCD
hardware.set_lcd("Auto-Water-Manager","BOOT...")

# Define Working Directory and Static Directory
base = os.getcwd()
staticdir  = base+"/static/"
templtdir  = base+"/views/"
filedir    = base+"/files/"
emaildir   = base+"/email/"

# Define Log Files and Error Log File
logfile    = filedir+"historiclog.csv"
logfileold = filedir+"historiclog_old.csv"
errlog     = filedir+"errorlog.txt"

# Define Email Template Files
new_log_notice  = emaildir+"newreport.emlx"
error_notice    = emaildir+"errnotice.emlx"
settings_notice = emaildir+"setnotice.emlx"

# Start Configuration Parser Object
configfile = 'config.ini'
parser = configparser.ConfigParser()
parser.read(configfile)
# Load settings for system
for section in parser.sections():
    for setting, value in parser.items(section):
        exec( str(setting) + '="' + str(value) + '"' )

# Declare Global Variable to Represent HTTP Communications Status
http_err = "None"
http_err_host = ""
####################################################################################



####################################################################################
# Define Push-Button Call-Back Functions
step = 0.01
def grn_callback(channel):
    global model
    # Count the Length of Time that the Button is Being Pressed
    t_cnt = 0
    while hardware.get_btn()[0]:
        t_cnt += step       # Increment Counter
        time.sleep(step)    # Sleep
        # Test for Reboot Criteria
        if all(hardware.get_btn()) and t_cnt>1:
            # Reboot System
            OsCommand('sudo reboot')
            hardware.set_led(grn=True,red=True)
            hardware.set_lcd("Rebooting...")
            modelTimer.stop()
            return
        elif t_cnt > 3:
            # Display Device IP Address
            hardware.set_lcd("IP: "+hardware.get_ip_adr())
            return
        elif t_cnt > 10:
            # Reboot System
            OsCommand('sudo reboot')
            hardware.set_led(grn=True,red=True)
            hardware.set_lcd("Rebooting...")
            modelTimer.stop()
            return
    # Start Control Model Updates
    model = system_model(hardware.get_temp()) # Re-Activate Model
    modelTimer.start()
    hardware.set_lcd("System-Enabled")
    CallThread(hardware.set_lcd,3,"System-OK",hardware.get_temp(fmt="{:.2f}'F"))
    hardware.set_led(grn=True,red=False)

def red_callback(channel):
    global model
    # Count the Length of Time that the Button is Being Pressed
    t_cnt = 0
    while hardware.get_btn()[1]:
        t_cnt += step       # Increment Counter
        time.sleep(step)    # Sleep
        # Test for Reboot Criteria
        if all(hardware.get_btn()) and t_cnt>1:
            # Reboot System
            OsCommand('sudo reboot')
            hardware.set_led(grn=True,red=True)
            hardware.set_lcd("Rebooting...")
            modelTimer.stop()
            return
        elif t_cnt > 10:
            # Shut Down System
            OsCommand('sudo shutdown')
            hardware.set_led(grn=False,red=True)
            hardware.set_lcd("Shutting-Down...")
            modelTimer.stop()
            return
    # Stop Control Model Updates
    model = None # Deactivate the Model
    modelTimer.stop()
    hardware.set_lcd("System-Disabled")
    hardware.set_led(grn=False,red=True)
####################################################################################



####################################################################################
# Define Model Update Function
def modelUpdate():
    # Use Try/Except to Catch Any Errors in Thread
    try:
        global http_err, http_err_host
        # Update LCD with Time and Temperature
        hardware.set_lcd(datetime.now().strftime("%d/%m/%Y-%H:%M"),
                         hardware.get_temp(fmt="{:.2f}'F"))
        # Collect Previous State
        prvStatus = model.get_state()
        # Set Force Off When Power Source Absent
        if not hardware.get_pwr_src()[0]:
            model.set_force("all",False,5)
        # Update Model
        model.update(hardware.get_temp())
        status = model.get_state()
        http_err = "None"
        http_err_host = ""
        # Send Message to Smart Plugs
        for ind,states in enumerate(zip(status,prvStatus)):
            # Extract from Tuple
            cur,prv = states
            if cur != prv:
                # Attempt Control
                try:
                    # Send Message to Smart Plug
                    rsp = outlet.tasmota_set(ind,cur)
                except:
                    rsp = False
                http_err = http_err or (not rsp)
                if not rsp:
                    http_err_host += '-'+outlet.host_lut[ind] # Append Host IP
                    model.set_fail(ind) # Reset Model to Account for Failure
        # Collect Date Time
        dt_str = datetime.now().strftime("%d/%m/%YT%H:%M:%S")
        # Generate Full CSV List for new Row
        csv_list = [dt_str, hardware.get_temp()]
        csv_list.extend(status)
        csv_list.extend([model.get_consumption(),http_err,http_err_host])
        # Count Rows in File
        try:
            with open(logfile, 'r') as file:
                # Count Number of Rows in File, Calculate Power and Avg Temp
                row_count = 0
                t_power = 0
                t_temp = 0
                # Iterate over each row
                for row in csv.reader(file, delimiter=','):
                    row_count += 1
                    # Skip the header, then sum the power and temp
                    if row_count > 1:
                        t_power += float(row[15])
                        t_temp += float(row[1])
                # Check for Over-Full File
                if row_count == 43200:
                    # Rename File, so New File Can Be Generated
                    os.rename(logfile, logfileold)
                    # Evaluate Average Temperature and Total Power
                    tot_power = t_power/60
                    avg_temp = t_temp/(row_count-1)
                    # If Log Messages are Enabled, Send Email Messages
                    if enlogmsg:
                        c_dict = {'power_kw':tot_power, 'avg_temp':avg_temp}
                        content = emailtemplate(new_log_notice,
                                                bodycontext=c_dict)
                        send_email([emailadd1,emailadd2,emailadd3],content,logfileold)
                    # Reset Row Count
                    row_count = 0
        except FileNotFoundError:
            row_count = 0
        # Write to File as Necessary
        with open(logfile, 'a') as file:
            # Generate Reader/Writer Objects
            file_writer = csv.writer(file, delimiter=',')
            # Perform Special Operations for First Row
            if row_count < 1:
                file_writer.writerow(["DateTime","Temperature","Pole1A","Pole1B",
                                      "Pole2A","Pole2B","Pole3A","Pole3B",
                                      "Pole4A","Pole4B","Pole5A","Pole5B",
                                      "Pole6A","Pole6B","StockPole",
                                      "PowerConsumption(kW-min)","HTTP-ERR","HOST-IP"])
            file_writer.writerow(csv_list)
    except:
        hardware.set_led(red=True)
        hardware.set_lcd("ERROR:Model","")
        # If Error Messages Are Enabled, Send Email Message
        if enerrmsg:
            errcont = emailtemplate(error_notice,
                                    bodycontext={'notice':
                                    "Exception in Temperature Model Update."})
            send_email([emailadd1,emailadd2,emailadd3],errcont)
####################################################################################



####################################################################################
# Define Temperature Retrieval Function
def get_temp():
    temp = round(hardware.get_temp(),2)
    return(str(temp))

# Define Light Status Retrieval Function
def get_light():
    rStatus = hardware.get_rly()
    if rStatus[lightRelay]:
        light = "ON"
    else:
        light = "OFF"
    return(light)

# Define Tri-State Status Function
def tristatus(trough):
    # Define Look-Up Table
    lut = [
            p1aserv,p1bserv,p2aserv,p2bserv,p3aserv,p3bserv,p4aserv,
            p4bserv,p5aserv,p5bserv,p6aserv,p6bserv,stockserv,
          ]
    # Test for Disabled (Out of Service), or Model is Deactivated
    if lut[trough] == 'None' or model==None:
        return("DISABLED")
    # Extract State from Model
    status = model.get_state()[trough]
    if status: # Heater is Enabled
        return("ON")
    else:
        return("OFF")
    # Catch All
    # If Error Messages Are Enabled, Send Email Message
    if enerrmsg:
        errcont = emailtemplate(error_notice,
                                bodycontext={'notice':
                                             "Exception in Web Response Update."})
        CallThread(send_email,0,[emailadd1,emailadd2,emailadd3],errcont)
    return("ERROR")
####################################################################################



####################################################################################
# Define and route Static Files (Images)
@Webapp.route('/static/<page>/<filename>')
@Webapp.route('/static/<filename>')
def serve_static(filename,page=None):
    if(page==None):
        return(static_file(filename, root=staticdir))
    else:
        return(static_file(page, root=staticdir))

# Define and route File Server
@Webapp.route('/files/<filename>')
def serve_files(filename):
    return(static_file(filename, root=filedir))

# Define Template-in-Template Function
def serve_template( label, layer0, layer1=None, layer2=None):
    if(layer1 is not None):
        if(layer2 is not None):
            body = template(layer1, BODY = layer2)
        else:
            body = template(layer1)
    else:
        body = ''
    return( template(layer0, BODY = body, PAGE = label) )

# Define API Data Retrieval
@Webapp.route('/api/status/<item>')
@Webapp.route('/api/status')
def api_status(item=None):
    global api_tags
    if item==None:
        api_tags = {
            'temp':get_temp(),'light':get_light(), 'daylight':hardware.get_photo(),
            'batlevel':hardware.get_bat_chg(),'batvolt':round(hardware.get_voltage(),2),
            'hosterrors':http_err,'activesrc':hardware.get_pwr_src()[0],
            'modelSta':str(hardware.get_led()[0]),
            'pole1a': tristatus(0), 'nam1a':animal1a,
            'pole1b': tristatus(1), 'nam1b':animal1b,
            'pole2a': tristatus(2), 'nam2a':animal2a,
            'pole2b': tristatus(3), 'nam2b':animal2b,
            'pole3a': tristatus(4), 'nam3a':animal3a,
            'pole3b': tristatus(5), 'nam3b':animal3b,
            'pole4a': tristatus(6), 'nam4a':animal4a,
            'pole4b': tristatus(7), 'nam4b':animal4b,
            'pole5a': tristatus(8), 'nam5a':animal5a,
            'pole5b': tristatus(9),'nam5b':animal5b,
            'pole6a': tristatus(10),'nam6a':animal6a,
            'pole6b': tristatus(11),'nam6b':animal6b,
            'stockpole':tristatus(12),'namstock':animalstock,
            'p1acheck':p1aserv, '1apower':power1a, 'size1a':size1a,
            'p1bcheck':p1bserv, '1bpower':power1b, 'size1b':size1b,
            'p2acheck':p2aserv, '2apower':power2a, 'size2a':size2a,
            'p2bcheck':p2bserv, '2bpower':power2b, 'size2b':size2b,
            'p3acheck':p3aserv, '3apower':power3a, 'size3a':size3a,
            'p3bcheck':p3bserv, '3bpower':power3b, 'size3b':size3b,
            'p4acheck':p4aserv, '4apower':power4a, 'size4a':size4a,
            'p4bcheck':p4bserv, '4bpower':power4b, 'size4b':size4b,
            'p5acheck':p5aserv, '5apower':power5a, 'size5a':size5a,
            'p5bcheck':p5bserv, '5bpower':power5b, 'size5b':size5b,
            'p6acheck':p6aserv, '6apower':power6a, 'size6a':size6a,
            'p6bcheck':p6bserv, '6bpower':power6b, 'size6b':size6b,
            'stockcheck':stockserv, 'stockpower':stockpower, 'sizestock':sizestock,
            'emailadd1':emailadd1, 'emailadd2':emailadd2, 'emailadd3':emailadd3,
            'enlogmsg':enlogmsg, 'enerrmsg':enerrmsg, 'ensetmsg':ensetmsg,
            'buttons':hardware.get_btn(),'lcd':hardware.get_lcd(),
            'leds':hardware.get_led(),'relays':hardware.get_rly(),
            'current':hardware.get_current(),'battery_led':hardware.get_bat_led(),
                   }
        return(api_tags)
    else:
        try:
            exec("global api_tags; api_tags = {'"+item+"':"+str(item)+"}")
            return(api_tags)
        except:
            return({item:"Invalid Request"})

@Webapp.route('/')
@Webapp.route('/index')
@Webapp.route('/index/')
@Webapp.route('/index.html')
def index():
    # Identify Presence of "Old" Log File
    if os.path.isfile( logfileold ):
        oldlog = """<a href="/static/historiclog_old.csv" download="log_old.csv">
                              <p><img src="/static/log.png" alt="Download" width="50"></p>
                              <p>Log File</p>
                            </a>"""
    else:
        oldlog = ""
    # Define Template Dictionary
    tags = {
        'temp':get_temp(),'light':get_light(), 'daylight':hardware.get_photo(),
        'batlevel':hardware.get_bat_chg(),'batvolt':round(hardware.get_voltage(),2),
        'hosterrors':http_err,'activesrc':hardware.get_pwr_src()[0],
        'modelSta':str(hardware.get_led()[0]),'oldlog':oldlog,
        'pole1a': tristatus(0), 'nam1a':animal1a,
        'pole1b': tristatus(1), 'nam1b':animal1b,
        'pole2a': tristatus(2), 'nam2a':animal2a,
        'pole2b': tristatus(3), 'nam2b':animal2b,
        'pole3a': tristatus(4), 'nam3a':animal3a,
        'pole3b': tristatus(5), 'nam3b':animal3b,
        'pole4a': tristatus(6), 'nam4a':animal4a,
        'pole4b': tristatus(7), 'nam4b':animal4b,
        'pole5a': tristatus(8), 'nam5a':animal5a,
        'pole5b': tristatus(9),'nam5b':animal5b,
        'pole6a': tristatus(10),'nam6a':animal6a,
        'pole6b': tristatus(11),'nam6b':animal6b,
        'stockpole':tristatus(12),'namstock':animalstock,
    }
    html = serve_template( tags, index_page )
    return( html )

@Webapp.route('/settings')
@Webapp.route('/settings/')
@Webapp.route('/settings.html')
def setpage():
    # Define Template Dictionary
    tags = {
        'p1acheck':p1aserv, '1apower':power1a, 'size1a':size1a, 'animal1a':animal1a,
        'p1bcheck':p1bserv, '1bpower':power1b, 'size1b':size1b, 'animal1b':animal1b,
        'p2acheck':p2aserv, '2apower':power2a, 'size2a':size2a, 'animal2a':animal2a,
        'p2bcheck':p2bserv, '2bpower':power2b, 'size2b':size2b, 'animal2b':animal2b,
        'p3acheck':p3aserv, '3apower':power3a, 'size3a':size3a, 'animal3a':animal3a,
        'p3bcheck':p3bserv, '3bpower':power3b, 'size3b':size3b, 'animal3b':animal3b,
        'p4acheck':p4aserv, '4apower':power4a, 'size4a':size4a, 'animal4a':animal4a,
        'p4bcheck':p4bserv, '4bpower':power4b, 'size4b':size4b, 'animal4b':animal4b,
        'p5acheck':p5aserv, '5apower':power5a, 'size5a':size5a, 'animal5a':animal5a,
        'p5bcheck':p5bserv, '5bpower':power5b, 'size5b':size5b, 'animal5b':animal5b,
        'p6acheck':p6aserv, '6apower':power6a, 'size6a':size6a, 'animal6a':animal6a,
        'p6bcheck':p6bserv, '6bpower':power6b, 'size6b':size6b, 'animal6b':animal6b,
        'stockcheck':stockserv, 'stockpower':stockpower, 'sizestock':sizestock, 'animalstock':animalstock,
        'emailadd1':emailadd1, 'emailadd2':emailadd2, 'emailadd3':emailadd3,
        'enlogmsg':enlogmsg, 'enerrmsg':enerrmsg, 'ensetmsg':ensetmsg,
    }
    html = serve_template( tags, settings_page )
    return( html )

@Webapp.route('/autowater_update', method='GET')
def update_settings():
    # Define all Global Variables
    global p1aserv, p1bserv, p2aserv, p2bserv, p3aserv, p3bserv
    global p4aserv, p4bserv, p5aserv, p5bserv, p6aserv, p6bserv
    global stockserv, power1a, power1b, power2a, power2b, power3a
    global power3b, power4a, power4b, power5a, power5b, power6a
    global power6b, stockpower, animal1a, animal1b, animal2a
    global animal2b, animal3a, animal3b, animal4a, animal4b
    global animal5a, animal5b, animal6a, animal6b, animalstock
    global size1a, size1b, size2a, size2b, size3a, size3b, size4a
    global size4b, size5a, size5b, size6a, size6b, sizestock, model
    # Mask Method Call Handle
    def get(q):
        return(str(request.query.get(q)))
    # Identify In/Out of Service
    p1aserv = get('pole1aservice')
    p1bserv = get('pole1bservice')
    p2aserv = get('pole2aservice')
    p2bserv = get('pole2bservice')
    p3aserv = get('pole3aservice')
    p3bserv = get('pole3bservice')
    p4aserv = get('pole4aservice')
    p4bserv = get('pole4bservice')
    p5aserv = get('pole5aservice')
    p5bserv = get('pole5bservice')
    p6aserv = get('pole6aservice')
    p6bserv = get('pole6bservice')
    stockserv = get('stockpoleservice')
    # Identify Power Settings
    power1a = get('power1a')
    power1b = get('power1b')
    power2a = get('power2a')
    power2b = get('power2b')
    power3a = get('power3a')
    power3b = get('power3b')
    power4a = get('power4a')
    power4b = get('power4b')
    power5a = get('power5a')
    power5b = get('power5b')
    power6a = get('power6a')
    power6b = get('power6b')
    stockpower = get('stockpolepower')
    # Identify Trough Size
    size1a = get('size1a')
    size1b = get('size1b')
    size2a = get('size2a')
    size2b = get('size2b')
    size3a = get('size3a')
    size3b = get('size3b')
    size4a = get('size4a')
    size4b = get('size4b')
    size5a = get('size5a')
    size5b = get('size5b')
    size6a = get('size6a')
    size6b = get('size6b')
    sizestock = get('sizestock')
    # Identify Animal Name
    animal1a = get('animal1a')
    animal1b = get('animal1b')
    animal2a = get('animal2a')
    animal2b = get('animal2b')
    animal3a = get('animal3a')
    animal3b = get('animal3b')
    animal4a = get('animal4a')
    animal4b = get('animal4b')
    animal5a = get('animal5a')
    animal5b = get('animal5b')
    animal6a = get('animal6a')
    animal6b = get('animal6b')
    animalstock = get('animalstock')
    # Prepare Settings
    for section in ["in-service","heaters","tanks","names"]:
        for setting, value in parser.items(section):
            exec( 'parser.set("'+str(section)+'","'+
                  str(setting)+'", str('+str(setting)+'))' )
    # Write File
    with open( configfile, 'w' ) as file:
                parser.write( file )
    if ensetmsg:
        # Configure List of Tags for Email Update
        tags = {
            'p1acheck':p1aserv, '1apower':power1a, 'size1a':size1a, 'animal1a':animal1a,
            'p1bcheck':p1bserv, '1bpower':power1b, 'size1b':size1b, 'animal1b':animal1b,
            'p2acheck':p2aserv, '2apower':power2a, 'size2a':size2a, 'animal2a':animal2a,
            'p2bcheck':p2bserv, '2bpower':power2b, 'size2b':size2b, 'animal2b':animal2b,
            'p3acheck':p3aserv, '3apower':power3a, 'size3a':size3a, 'animal3a':animal3a,
            'p3bcheck':p3bserv, '3bpower':power3b, 'size3b':size3b, 'animal3b':animal3b,
            'p4acheck':p4aserv, '4apower':power4a, 'size4a':size4a, 'animal4a':animal4a,
            'p4bcheck':p4bserv, '4bpower':power4b, 'size4b':size4b, 'animal4b':animal4b,
            'p5acheck':p5aserv, '5apower':power5a, 'size5a':size5a, 'animal5a':animal5a,
            'p5bcheck':p5bserv, '5bpower':power5b, 'size5b':size5b, 'animal5b':animal5b,
            'p6acheck':p6aserv, '6apower':power6a, 'size6a':size6a, 'animal6a':animal6a,
            'p6bcheck':p6bserv, '6bpower':power6b, 'size6b':size6b, 'animal6b':animal6b,
            'stockcheck':stockserv, 'stockpower':stockpower, 'sizestock':sizestock, 'animalstock':animalstock,
            'emailadd1':emailadd1, 'emailadd2':emailadd2, 'emailadd3':emailadd3,
        }
        for key,value in tags.items():
            if value=='checked':
                tags[key] = 'True'
            elif value=='None':
                tags[key] = 'False'
        # Build Settings Notice
        emlx = emailtemplate(settings_notice,htmlcontext=tags)
        # Send Email
        CallThread(send_email,0,[emailadd1,emailadd2,emailadd3],emlx)
    # Capture Current Temperatures for Update
    curTemperature = model.get_temp()
    # Re-Instantiate Model with new Parameters
    model = system_model(hardware.get_temp(),t0=curTemperature)
    # Update Front LED's As Necessary
    hardware.set_led(grn=True,red=False)
    # Restart Model Timer
    modelTimer.restart()
    redirect('/settings')

@Webapp.route('/force_heater/<force>/<state>/<heaterind>', method='GET')
def force_heaters(force,state,heaterind):
    time_set = float(force)*60
    option = {"ON":True,"OFF":False}[state]
    heater_ind = int(heaterind)
    # Do Force with Model
    try:
        model.set_force(heater_ind,option,time_set)
        modelUpdate() # Update Model (will inherently cause some minor inaccuracy)
    except:
        # If Error Messages Are Enabled, Send Email Message
        if enerrmsg:
            errcont = emailtemplate(error_notice,
                                    bodycontext={'notice':
                                    "\nHeater force attempted on disabled system.\n"+
                                    "Please re-enable system before forcing heaters."})
            send_email([emailadd1,emailadd2,emailadd3],errcont)
    redirect('/settings')

@Webapp.route('/email_update', method='GET')
def update_email():
    # Define all Global Variables
    global emailadd1, emailadd2, emailadd3
    global enlogmsg, enerrmsg, ensetmsg
    # Update Variables
    emailadd1 = request.query.get('emailadd1')
    emailadd2 = request.query.get('emailadd2')
    emailadd3 = request.query.get('emailadd3')
    enlogmsg = request.query.get('enlogmsg')
    enerrmsg = request.query.get('enerrmsg')
    ensetmsg = request.query.get('ensetmsg')
    # Save Settings
    parser.set('email','emailadd1', emailadd1)
    parser.set('email','emailadd2', emailadd2)
    parser.set('email','emailadd3', emailadd3)
    parser.set('email','enlogmsg', str(enlogmsg))
    parser.set('email','enerrmsg', str(enerrmsg))
    parser.set('email','ensetmsg', str(ensetmsg))
    # Write File
    with open( configfile, 'w' ) as file:
                parser.write( file )
    redirect('/settings')

@Webapp.route('/set_light', method='get')
def control_barn_light():
    # Toggle the Barn Light
    rStatus = hardware.get_rly()[lightRelay]
    hardware.set_rly(lightRelay,(not rStatus))
    redirect('/')

# Define Authenticator Function Using PAM
def confirm_user(user, password):
    try:
        auth = pam.pam()
        if not (auth.authenticate(user, password)):
            print("Unauthorized Control Attempt!")
            abort(code=403)
        else:
            return(True)
    except:
        abort(code=403)
# Define Delete Log Files Page
@Webapp.route('/deletelogs')
@Webapp.route('/deletelog')
@Webapp.route('/delete')
@auth_basic(confirm_user)
def delete_log_files():
    # Attempt Deleting Files that May (or may not) be Present
    # Logfile
    try:
        os.remove(logfile)
    except:
        pass
    # Previous Period Log File
    try:
        os.remove(logfileold)
    except:
        pass
    redirect('/') # Return to Index
# Define Refresh Code Functional Operation
@Webapp.route('/gitpull')
@Webapp.route('/git')
@auth_basic(confirm_user)
def upgrade_code(servicerestart=True):
    # Passed Credentials, Perform Update
    repo = git.Git()
    status = repo.pull()
    if servicerestart:
        OsCommand('sudo service AutoWaterWeb restart')
        return(status)
# Define Upgrade Routing and Functional Operation for Upgrade
@Webapp.route('/upgrade')
@Webapp.route('/update')
@auth_basic(confirm_user)
def upgrade_server():
    # Passed Credentials, Perform Upgrade to Codebase
    upgrade_code(servicerestart=False)
    # Perform System Update and Upgrade, One-Shot
    cmd = OsCommand('sudo apt-get update && sudo apt-get upgrade -y',True,0)
    response = cmd.run()
    # Reboot System
    OsCommand('sudo reboot')
    return(response)
####################################################################################



####################################################################################
@Webapp.error(404)
def error404(error):
    return( serve_static("404err.html") )
@Webapp.error(403)
def error403(error):
    return( serve_static("403err.html") )
@Webapp.error(500)
def error500(error):
    return( serve_static("500err.html") )
####################################################################################



####################################################################################
# Run Main Server
try:
    hardware.set_led(grn=True) # Set Green LED to Indicate Active Status
    hardware.set_lcd("System-OK",hardware.get_temp(fmt="{:.2f}'F")) # Update LCD
    # Start Model Timer to Manage Updates, Load Temperature Each Time
    modelTimer = RepeatedThread(60, modelUpdate)
    # Assocaite Push-Button Call-Back Functions with Hardware Callback
    hardware.set_grn_callback(grn_callback)
    hardware.set_red_callback(red_callback)
    # Start Web-App
    Webapp.run(host=hostname, port=port)
except:
    # An Internal Error has Occurred and the Server has Died!
    hardware.set_lcd("SERVER-CRASHED!")
    hardware.set_led(True,True)
    modelTimer.stop()
    # If Error Messages Are Enabled, Send Email Message
    if enerrmsg:
        errcont = emailtemplate(error_notice,
                                bodycontext={'notice':
                                "Web Server Crashed! Manual Restart Required"})
        send_email([emailadd1,emailadd2,emailadd3],errcont)
finally:
    # Regardless of Error or Quit, Stop Timer for Model Operation
    modelTimer.stop()
####################################################################################
# END