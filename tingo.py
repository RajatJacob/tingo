import paho.mqtt.client as mqtt
from conf import *
from animations import *

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
	#print("Connected with result code "+str(rc))
	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
	client.subscribe("tingo/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	topic = msg.topic.split('/')
	dev_id = topic[1]
	confFile = globals()[dev_id]
	typeClass = getattr(globals()[confFile.conf["type"]], confFile.conf["type"])(confFile.conf["pin"])
	getattr(typeClass, topic[2])(msg.payload)

client = mqtt.Client()
client.username_pw_set(broker.conf['username'], broker.conf['password'])
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker.conf['addr'], broker.conf['port'], 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()