import yaml
import functions
import paho.mqtt.client as mqtt
import RPi.GPIO as gpio

config = yaml.load(open("config.yaml"), Loader=yaml.FullLoader)
broker = config.get('broker', {})
devices = config.get('devices', [])
topics = [device.get('topic') for device in devices]


def on_connect(client, userdata, flags, rc):
    for t in topics:
        client.subscribe(t)


def on_message(client, userdata, msg):
    idx = topics.index(msg.topic)
    if idx != -1:
        dev = devices[idx]
        functions.call(dev, msg.payload)

def setupGPIO():
    gpio.setwarnings(False)
    gpio.setmode(gpio.BCM)
    outputTypes = ['toggleable']
    inputTypes = []
    for dev in devices:
        if dev.get('type') in outputTypes:
            gpio.setup(dev.get('pin'), gpio.OUT)
        elif dev.get('type') in inputTypes:
            gpio.set(dev.get('pin'), gpio.IN)

setupGPIO()

client = mqtt.Client()
client.username_pw_set(broker.get('username'), broker.get('password'))
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker.get('host'), broker.get('port'), 60)

client.loop_forever()
