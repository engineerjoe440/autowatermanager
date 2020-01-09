from RPLCD import CharLCD
import RPi.GPIO as GPIO
import time

lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=24, rows=1, pin_rs=21, pin_e=23, pins_data=[29,35,31,33])
time.sleep(1)
lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=24, rows=1, pin_rs=21, pin_e=23, pins_data=[29,35,31,33])

try:
    print("starting")
    while True:
        lcd.write_string('Hello\0World!')
        time.sleep(1)
        lcd.clear()
        lcd.write_string('\0\0\1\2\3\4\13\13\13\13\13\13\13\13\13\13Joe\0Stanley')
        time.sleep(1)
        lcd.clear()

finally:
    GPIO.cleanup()