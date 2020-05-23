import json
import RPi.GPIO as GPIO
from devices import DigitalDevice

with open(".conf.json", "r") as confFile:
	conf = json.load(confFile)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

devices = {}

for d in conf['devices']:
	if d['type'].lower().strip() == "digital":
		devices[d['name']] = DigitalDevice(int(d['pin']), GPIO.IN if d['mode'] == 'input' else GPIO.OUT)


states = [True, False]*3
import time

for d in devices:
	for s in states:
		devices[d].setState(s)
		time.sleep(0.5)
