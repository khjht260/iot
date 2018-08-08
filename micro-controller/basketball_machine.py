import RPi.GPIO as GPIO

import time


ledPIN = 12
print('Setup Pin', ledPIN)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPIN, GPIO.OUT)


def activate():
    GPIO.output(ledPIN, True)
    time.sleep(5)
    GPIO.output(ledPIN, False)
    
    return "True"