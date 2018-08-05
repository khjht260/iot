import RPi.GPIO as GPIO
import time
from sys import argv

ledPIN = int(argv[1])

GPIO.setmode(GPIO.BOARD)
print('Setup Pin', ledPIN)
GPIO.setup(ledPIN, GPIO.OUT)

while True:
    GPIO.output(ledPIN, False)
    time.sleep(1)

    GPIO.output(ledPIN, True)
    time.sleep(1)
