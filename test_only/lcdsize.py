from RPLCD import CharLCD
import RPi.GPIO as GPIO
import time

lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=24, rows=2, pin_rs=21, pin_e=23, pins_data=[29,35,31,33])
time.sleep(1)
lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=24, rows=2, pin_rs=21, pin_e=23, pins_data=[29,35,31,33])

try:
    print("starting")
    NL = 16*' '
    x = 0
    while True:
        spc = ' '*x
        x += 1
        lcd.write_string(spc+'World!\x0dHello\0Joe\0Stanley')
        time.sleep(1)
        lcd.clear()

finally:
    GPIO.cleanup()
