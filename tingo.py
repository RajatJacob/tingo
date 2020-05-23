import RPi.GPIO as GPIO
from devices import DigitalDevice

GPIO.setmode(GPIO.BCM)

lamp = DigitalDevice(16, GPIO.OUT)

print(lamp.getState())

lamp.setState(True)

print(lamp.getState())

lamp.setState(False)

print(lamp.getState())
