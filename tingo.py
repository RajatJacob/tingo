import json
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
from devices import DigitalDevice

# READ CONFIG FILE
with open(".conf.json", "r") as confFile:
	conf = json.load(confFile)

# GPIO SETUP
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# DEVICE INITIALISATION
devices = {}
for d in conf['devices']:
	if d['type'].lower().strip() == "digital":
		devices[d['name']] = DigitalDevice(int(d['pin']), GPIO.IN if d['mode'] == 'input' else GPIO.OUT, setState=False)

# MQTT CALLBACKS
def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	for d in conf['devices']:
		topic = d['topic']
		if topic is not None:
			client.subscribe(topic)
		else:
			print(topic)

def on_message(client, userdata, msg):
	for d in conf['devices']:
		if d['topic'] == msg.topic:
			devices[d['name']].setState(msg.payload)

# MQTT SETUP
client = mqtt.Client(client_id=conf["broker"]["client_id"], clean_session=False)
client.on_connect = on_connect
client.on_message = on_message
client.connect(conf['broker']['host'], conf['broker']['port'], 60)
client.loop_forever()



# EXTRA

states = [True, False]*3
import time

for d in devices:
	for s in states:
		devices[d].setState(s)
		time.sleep(0.5)
