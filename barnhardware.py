# Barn Automation Hardware Interface
import threading
import time
import sys

try:
    from RPLCD import CharLCD
    import RPi.GPIO as GPIO
except:
    print("Failed to import. Testing on Windows? Try on RPi!")
    time.sleep(5)
    sys.exit()

# Define Shared (Global) Variable
lcdmsg = ''

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
# Define Add'l GPIO Pins
gLED = 15
rLED = 19
gBTN = 11
rBTN = 13
# Define Add'l Parameters
start_time = 0.1

class BarnHardware:
    def __init__(self,td=0.5):
        self.time = td
        # Initialize LCD Display
        self.lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=col, rows=row,
                           pin_rs=rs, pin_e=en, pins_data=[d4,d5,d6,d7])
        time.sleep(start_time)
        self.lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=col, rows=row,
                           pin_rs=rs, pin_e=en, pins_data=[d4,d5,d6,d7])
        # Initialize Button and LED GPIO Pins
        GPIO.setup(gLED, GPIO.OUT, initial=0)
        GPIO.setup(rLED, GPIO.OUT, initial=0)
        GPIO.setup(gBTN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(rBTN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        # Init Complete, Start Running
        self.run()
    
    # Define Get Functions
    def get_btn(self):
        grn = GPIO.input(gBTN) == GPIO.HIGH
        red = GPIO.input(rBTN) == GPIO.HIGH
        return(grn,red)
    def get_lcd(self):
        global lcdmsg
        return(lcdmsg.replace('\0',' ').replace('\x10','\n'))
    
    # Define Callback Specifiers
    def set_grn_callback(self,func,opt=GPIO.HIGH):
        GPIO.add_event_detect(gBTN,opt,callback=func)
    def set_red_callback(self,func,opt=GPIO.HIGH):
        GPIO.add_event_detect(rBTN,opt,callback=func)
    
    # Define Set Functions for LED's and LCD
    def set_led(self,grn=False,red=False):
        global lcdmsg
        # Set LEDs
        GPIO.output(gLED,grn)
        GPIO.output(rLED,red)
    def set_lcd(self,LINE1,LINE2):
        global lcdmsg
        NL = 16*' ' # 16 Spaces
        # Condition Inputs
        LINE1 = LINE1[:col].replace(' ','\0')
        LINE2 = LINE2[:col].replace(' ','\0')
        msg = NL + LINE2 + '\r' + LINE1
        lcdmsg = msg
    
    # Define LCD Operating Function
    def run(self):
        global lcdmsg
        try:
            if __name__ == '__main__':
                print("testing...",len(lcdmsg))
            # Clear LCD
            self.lcd.clear()
            # Write Message
            self.lcd.write_string(lcdmsg)
            # Start Threading Timer
            threading.Timer(self.time, self.run).start()
        except:
            GPIO.cleanup()

# Define Test Method
if __name__ == '__main__':
    try:
        hdw = BarnHardware()
        hdw.set_lcd("Hello World! TESTING...","From:_Joe_Stanley")
        while(True):
            time.sleep(1)
    finally:
        GPIO.cleanup()