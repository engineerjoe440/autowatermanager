# Barn Automation Outlet Operation Script

# Import Required Libraries
import requests
import json

# Define State Look-Up-Table
state_lut = {False:'OFF', True:'ON'}

# Define Network Parameters
domain = "192.168.220"

# Define Hosts
heater1a = int("1A",16)
heater1b = int("1B",16)
heater2a = int("2A",16)
heater2b = int("2B",16)
heater3a = int("3A",16)
heater3b = int("3B",16)
heater4a = int("4A",16)
heater4b = int("4B",16)
heater5a = int("5A",16)
heater5b = int("5B",16)
heater6a = int("6A",16)
heater6b = int("6B",16)
heater_stock = 120

# Define Set function
def tasmota_set(host, state):
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