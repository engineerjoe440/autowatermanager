########################################################################
#  AutoWaterManager Main Operating Web Server
#  (c) Stanley Solutions
#  Joe Stanley - engineerjoe440@yahoo.com
########################################################################

# Define Parameters
hostname = '0.0.0.0'
port = 8085

# Define Static Parameters
index_page = 'index.tpl'
settings_page = 'settings.tpl'

# Import Dependencies
import os
from bottle import route, run, template, static_file, error, redirect

# Define Working Directory and Static Directory
base = os.getcwd()
staticdir = base+"/static/"
templtdir = base+"/views/"
filedir   = base+"/files/"

# Define and route Static Files (Images):
@route('/static/<page>/<filename>')
@route('/static/<filename>')
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

@route('/')
@route('/index')
@route('/index/')
@route('/index.html')
def index():
    # Define Template Dictionary
    tags = {
        'temp':     '32',
        'pole1a':   '',
        'pole1b':   '',
        'pole2a':   '',
        'pole2b':   '',
        'pole3a':   '',
        'pole3b':   '',
        'pole4a':   '',
        'pole4b':   '',
        'pole5a':   '',
        'pole5b':   '',
        'pole6a':   '',
        'pole6b':   '',
        'stockpole':'',
    }
    html = serve_template( tags, index_page )
    return( html )

@route('/settings')
@route('/settings/')
@route('/settings.html')
def setpage():
    # Define Template Dictionary
    tags = {
        '1apower': '500',
        '1bpower': '500',
        '2apower': '500',
        '2bpower': '500',
        '3apower': '500',
        '3bpower': '500',
        '4apower': '500',
        '4bpower': '500',
        '5apower': '500',
        '5bpower': '500',
        '6apower': '500',
        '6bpower': '500',
        'stockpower': '750',
    }
    html = serve_template( tags, settings_page )
    return( html )

@route('/autowater_update')
def update():
    redirect('/settings')

@error(404)
def error404(error):
    return( serve_static("404err.html") )

# Run Main Server
run(host=hostname, port=port, reloader=True)