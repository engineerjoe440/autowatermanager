########################################################################
#  AutoWaterManager Main Operating Web Server
#  (c) Stanley Solutions
#  Joe Stanley - engineerjoe440@yahoo.com
########################################################################

# Define Parameters
hostname = 'localhost'
port = 8085

# Define Static Parameters
index_page = 'index.html'
settings_page = 'settings.html'

# Import Dependencies
from bottle import route, run, template, static_file

@route('/')
@route('/index')
@route('/index/')
def index():
    html = static_file( index_page, root='./test site/')
    return( html )
    

# Run Main Server
run(host=hostname, port=port)