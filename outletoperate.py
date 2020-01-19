# Barn Automation Outlet Operation Script

# Import Required Libraries
import requests
import json

# Define Network Parameters
domain = "192.168.220."

# Define Hosts
heater1a = str(int("1A",16))
heater1b = str(int("1B",16))
heater2a = str(int("2A",16))
heater2b = str(int("2B",16))
heater3a = str(int("3A",16))
heater3b = str(int("3B",16))
heater4a = str(int("4A",16))
heater4b = str(int("4B",16))
heater5a = str(int("5A",16))
heater5b = str(int("5B",16))
heater6a = str(int("6A",16))
heater6b = str(int("6B",16))
heater_stock = str(120)

# Define Look-Up-Tables
state_lut = {False:'OFF', True:'ON'}
host_lut  = [domain+heater1a,domain+heater1b,domain+heater2a,domain+heater2b,
             domain+heater3a,domain+heater3b,domain+heater4a,domain+heater4b,
             domain+heater5a,domain+heater5b,domain+heater6a,domain+heater6b,
             domain+heater_stock]

# Define Set function
def tasmota_set(host, state):
    # Interpret Host if Provided as Integer
    if isinstance(host,int):
        host = host_lut[host]
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
    import time
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