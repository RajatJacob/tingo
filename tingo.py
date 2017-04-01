import paho.mqtt.client as mqtt
import animations
import conf

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
	#print("Connected with result code "+str(rc))
	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
	client.subscribe("tingo/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	#print(msg.topic+": "+str(msg.payload))
<<<<<<< HEAD
	try:
		getattr(animations, msg.topic.split("/")[1])(str(msg.payload))
	except:
		pass
=======
	try:
		getattr(animations, msg.topic.split("/")[1])(str(msg.payload))
	except:
		pass
>>>>>>> 36ffd14ac5df140988fedb9a4cf766c5bb4c3f57

client = mqtt.Client()
client.username_pw_set(conf.broker['username'], conf.broker['password'])
client.on_connect = on_connect
client.on_message = on_message

client.connect(conf.broker['addr'], conf.broker['port'], 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
