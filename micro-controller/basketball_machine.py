import RPi.GPIO as GPIO

import time
from settings import pin_settings

active_pin = pin_settings['active_pin']
print('Setup Pin', active_pin)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(active_pin, GPIO.OUT)


def activate():
    GPIO.output(active_pin, True)
    time.sleep(0.1)
    GPIO.output(active_pin, False)
    
    return "True"