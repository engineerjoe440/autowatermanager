########################################################################
#  AutoWaterManager Main Operating Web Server
#  (c) Stanley Solutions
#  Joe Stanley - engineerjoe440@yahoo.com
########################################################################

# Define Parameters
hostname = '192.168.254.128'
port = 8085

# Define Static Parameters
index_page = 'index.html'
settings_page = 'settings.html'

# Import Dependencies
import os
from bottle import route, run, template, static_file, error

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
def index():
    html = static_file( index_page, root='./static/')
    return( html )

@error(404)
def error404(error):
    return( serve_static("404err.html") )

# Run Main Server
run(host=hostname, port=port, reloader=True)