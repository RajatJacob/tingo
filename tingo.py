import RPi.GPIO as GPIO
from devices import DigitalDevice

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

lamp = DigitalDevice(16, GPIO.OUT)


states = [True, False, True, False, True]

import time
for s in states:
	print(lamp.setState(s))
	time.sleep(1)
