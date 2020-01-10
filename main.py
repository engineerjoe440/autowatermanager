########################################################################
#  AutoWaterManager Main Operating Web Server
#  (c) Stanley Solutions
#  Joe Stanley - engineerjoe440@yahoo.com
########################################################################

# Define Parameters
hostname = '0.0.0.0'
port = 80

# Define Static Parameters
index_page = 'index.tpl'
settings_page = 'settings.tpl'

# Import Dependencies
import os
import git
from bottle import route, run, template, static_file, error
from bottle import request, redirect, Bottle, auth_basic, abort
import configparser
try:
    import pam
    from barnhardware import BarnHardware
except:
    print("WARNING! Seems you're testing on Windows. Some features won't work.")

# Instantiate Objects
Webapp = Bottle()

# Define Working Directory and Static Directory
base = os.getcwd()
staticdir = base+"/static/"
templtdir = base+"/views/"
filedir   = base+"/files/"

# Start Configuration Parser Object
configfile = 'config.ini'
parser = configparser.ConfigParser()
parser.read(configfile)
# Load settings for system
for section in parser.sections():
    for setting, value in parser.items(section):
        exec( str(setting) + '="' + str(value) + '"' )

# Define Temperature Retrieval Function
def get_temp():
    temp = 32
    return(str(temp))

# Define Light Status Retrieval Function
def get_light():
    light = "ON"
    return(light)

# Define Batter Status Retrieval Function
def get_battery():
    battery = "OK"
    return(battery)

# Define Tri-State Status Function
def tristatus(trough):
    if trough==1:
        if p1aserv == "None":
            return("DISABLED")
    elif trough==2:
        if p1bserv == "None":
            return("DISABLED")
    elif trough==3:
        if p2aserv == "None":
            return("DISABLED")
    elif trough==4:
        if p2bserv == "None":
            return("DISABLED")
    elif trough==5:
        if p3aserv == "None":
            return("DISABLED")
    elif trough==6:
        if p3bserv == "None":
            return("DISABLED")
    elif trough==7:
        if p4aserv == "None":
            return("DISABLED")
    elif trough==8:
        if p4bserv == "None":
            return("DISABLED")
    elif trough==9:
        if p5aserv == "None":
            return("DISABLED")
    elif trough==10:
        if p5bserv == "None":
            return("DISABLED")
    elif trough==11:
        if p6aserv == "None":
            return("DISABLED")
    elif trough==12:
        if p6bserv == "None":
            return("DISABLED")
    elif trough==13:
        if stockserv == "None":
            return("DISABLED")
    # Catch All
    return("ERROR")

# Define and route Static Files (Images):
@Webapp.route('/static/<page>/<filename>')
@Webapp.route('/static/<filename>')
def serve_static(filename,page=None):
    if(page==None):
        return(static_file(filename, root=staticdir))
    else:
        return(static_file(page, root=staticdir))

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

@Webapp.route('/')
@Webapp.route('/index')
@Webapp.route('/index/')
@Webapp.route('/index.html')
def index():
    # Validate Service State
    # Define Template Dictionary
    tags = {
        'temp':get_temp(),'light':get_light(),'bat':get_battery(),
        'pole1a': tristatus(1), 'nam1a':animal1a,
        'pole1b': tristatus(2), 'nam1b':animal1b,
        'pole2a': tristatus(3), 'nam2a':animal2a,
        'pole2b': tristatus(4), 'nam2b':animal2b,
        'pole3a': tristatus(5), 'nam3a':animal3a,
        'pole3b': tristatus(6), 'nam3b':animal3b,
        'pole4a': tristatus(7), 'nam4a':animal4a,
        'pole4b': tristatus(8), 'nam4b':animal4b,
        'pole5a': tristatus(9), 'nam5a':animal5a,
        'pole5b': tristatus(10),'nam5b':animal5b,
        'pole6a': tristatus(11),'nam6a':animal6a,
        'pole6b': tristatus(12),'nam6b':animal6b,
        'stockpole':tristatus(13),'namstock':animalstock,
    }
    html = serve_template( tags, index_page )
    return( html )

@Webapp.route('/settings')
@Webapp.route('/settings/')
@Webapp.route('/settings.html')
def setpage():
    # Define Template Dictionary
    tags = {
        'p1acheck':p1aserv, '1apower':power1a, 'animal1a':animal1a,
        'p1bcheck':p1bserv, '1bpower':power1b, 'animal1b':animal1b,
        'p2acheck':p2aserv, '2apower':power2a, 'animal2a':animal2a,
        'p2bcheck':p2bserv, '2bpower':power2b, 'animal2b':animal2b,
        'p3acheck':p3aserv, '3apower':power3a, 'animal3a':animal3a,
        'p3bcheck':p3bserv, '3bpower':power3b, 'animal3b':animal3b,
        'p4acheck':p4aserv, '4apower':power4a, 'animal4a':animal4a,
        'p4bcheck':p4bserv, '4bpower':power4b, 'animal4b':animal4b,
        'p5acheck':p5aserv, '5apower':power5a, 'animal5a':animal5a,
        'p5bcheck':p5bserv, '5bpower':power5b, 'animal5b':animal5b,
        'p6acheck':p6aserv, '6apower':power6a, 'animal6a':animal6a,
        'p6bcheck':p6bserv, '6bpower':power6b, 'animal6b':animal6b,
        'stockcheck':stockserv, 'stockpower':stockpower, 'animalstock':animalstock,
        'emailadd1':emailadd1, 'emailadd2':emailadd2, 'emailadd3':emailadd3,
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
    # Mask Method Call Handle
    get = request.query.get
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
    for section in ["in-service","heaters","names"]:
        for setting, value in parser.items(section):
            exec( 'parser.set("'+str(section)+'","'+
                  str(setting)+'", str('+str(setting)+'))' )
    # Write File
    with open( configfile, 'w' ) as file:
                parser.write( file )
    # Identify Manual Control
    
    redirect('/settings')

@Webapp.route('/email_update', method='GET')
def update_email():
    # Define all Global Variables
    global emailadd1, emailadd2, emailadd3
    # Update Variables
    emailadd1 = request.query.get('emailadd1')
    emailadd2 = request.query.get('emailadd2')
    emailadd3 = request.query.get('emailadd3')
    # Save Settings
    parser.set('email','emailadd1', emailadd1)
    parser.set('email','emailadd2', emailadd2)
    parser.set('email','emailadd3', emailadd3)
    # Write File
    with open( configfile, 'w' ) as file:
                parser.write( file )
    redirect('/settings')

@Webapp.route('/set_light', method='get')
def control_barn_light():
    # Toggle the Barn Light
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
# Define Refresh Code Functional Operation
@Webapp.route('/gitpull')
@auth_basic(confirm_user)
def upgrade_code():
    # Passed Credentials, Perform Update
    repo = git.Git()
    status = repo.pull()
    return(status)
# Define Upgrade Routing and Functional Operation for Upgrade
@Webapp.route('/upgrade')
@Webapp.route('/update')
@auth_basic(confirm_user)
def upgrade_server():
    # Passed Credentials, Perform Upgrade
    upgrade_code()
    

@Webapp.error(404)
def error404(error):
    return( serve_static("404err.html") )
@Webapp.error(403)
def error403(error):
    return( serve_static("403err.html") )
@Webapp.error(500)
def error500(error):
    return( serve_static("500err.html") )

# Run Main Server
Webapp.run(host=hostname, port=port)