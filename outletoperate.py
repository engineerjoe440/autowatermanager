# Barn Automation Outlet Operation Script
# WiFi Dongle Support: https://www.raspberrypi.org/forums/viewtopic.php?p=462982#p462982

# Import Required Libraries
import requests
import json
from pyping import ping

# Define Network Parameters
domain = "192.168.220."

# Define Hosts
host_prefix = 'tasmota-'
h1A = '6602'
h1B = '7236'
h2A = ''
h2B = '3199'
h3A = '6259'
h3B = ''
h4A = ''
h4B = '4426'
h5A = '2343'
h5B = ''
h6A = ''
h6B = '7377'
hstock = '3419'

# Define Look-Up-Tables
state_lut = {False:'OFF', True:'ON'}
hostname_lut  = [host_prefix+h1A,host_prefix+h1B,host_prefix+h2A,host_prefix+h2B,
                 host_prefix+h3A,host_prefix+h3B,host_prefix+h4A,host_prefix+h4B,
                 host_prefix+h5A,host_prefix+h5B,host_prefix+h6A,host_prefix+h6B,
                 host_prefix+hstock]
heater_lut = ['Heater1A','Heater1B','Heater2A','Heater2B','Heater3A','Heater3B',
              'Heater4A','Heater4B','Heater5A','Heater5B','Heater6A','Heater6B',
              'HeaterStock']
host_lut = {}

# Define "DNS Resolution" Function (Ping Resolver)
def resolve(host):
    # Ping the Host and Evaluate the IP
    try:
        for i in range(5):
            ip = ping(host).destination_ip
            if ip.startswith('192.168.220.'):
                host_lut[host] = ip
                return(True)
            else:
                print("Bad IP:",ip)
        host_lut[host] = None
        return(False)
    # Ping Attempt Failed... Record Failure
    except:
        host_lut[host] = None
        return(False)

# Define System-Wide Resolution Function (Used at Startup)
def resolve_all():
    # For Every Valid Hostname, Determine the IP
    for ind,hostname in enumerate(hostname_lut):
        # Identify a Friendly-Name for the Heater Control
        heater_id = heater_lut[ind]
        # If Valid Domain Name, Attempt Resolution
        if len(hostname) > 8:
            yield(heater_id,resolve(hostname))
        # Else Record Invalid "Object"
        else:
            host_lut[hostname] = None
            yield(heater_id,None)

# Define Set function
def tasmota_set(host, state):
    # Interpret Host if Provided as Integer
    if isinstance(host,int):
        hostname = hostname_lut[host]
        host = host_lut[hostname]
        if host == None:
            return(False)
    # Interpret State
    state = state_lut[bool(state)]
    # Generate Simple Control String for HTTP and Send
    uri = "http://{}/cm?cmnd=Power%20{}".format(str(host),str(state))
    response = requests.get(uri)
    # Check Response
    return(response.status_code == 200) # Return True/False

# Define Set On Function
def tasmota_turn_on(host):
    # Generate Simple Control String for HTTP and Send
    uri = "http://{}/cm?cmnd=Power%20On".format(str(host))
    response = requests.get(uri)
    # Check Response
    return(response.status_code == 200) # Return True/False

# Define Set Off Function
def tasmota_turn_off(host):
    # Generate Simple Control String for HTTP and Send
    uri = "http://{}/cm?cmnd=Power%20Off".format(str(host))
    response = requests.get(uri)
    # Check Response
    return(response.status_code == 200) # Return True/False

# Define Toggle Function
def tasmota_toggle(host):
    # Generate Simple Control String for HTTP and Send
    uri = "http://{}/cm?cmnd=Power%20TOGGLE".format(str(host))
    response = requests.get(uri)
    # Check Response
    return(response.status_code == 200) # Return True/False

# Define Status Retrieval Function
def tasmota_status(host, fullresponse=False):
    # Interpret Host if Provided as Integer
    if isinstance(host,int):
        hostname = hostname_lut[host]
        host = host_lut[hostname]
        if host == None:
            return(None)
    # Generate Simple URI to Request Status
    uri = "http://{}/cm?cmnd=status".format(str(host))
    # Request Status
    response = requests.get(uri).text
    # Return Full Response if Desired
    if fullresponse:
        return(json.loads(response))
    # Extract State
    state = json.loads( response )['Status']['Power']
    return(bool(state))

# Define Builtin Testing System
if __name__ == '__main__':
    print(host_lut)
    import time
    time.sleep(60)
    host = input("Please Specify a Test Host IP Address:  ")
    print("Current Status:",state_lut[tasmota_status(host)])
    time.sleep(2)
    print("Turning On...")
    tasmota_turn_on(host)
    time.sleep(2)
    print("Turning Off...")
    tasmota_turn_off(host)
    time.sleep(2)
    print("Toggling...")
    tasmota_toggle(host)
    time.sleep(2)
    x = int(input("Specify Control (as integer):  "))
    while int(x) >= 0:
        tasmota_set(host,x)
        x = int(input("Specify Control (as integer):  "))

# END