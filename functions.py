import RPi.GPIO as gpio
import rpi_ws281x as neo


def toggleable(device, msg):
    gpio.output(device['pin'], gpio.LOW if msg.payload !=
                b'false' else gpio.HIGH)


devObj = {}

GAMMA_CORRECT_FACTOR = 2.8


def gamma(led_val):
    max_val = (1 << 8) - 1.0
    corrected = pow(led_val / max_val, GAMMA_CORRECT_FACTOR) * max_val
    return int(min(255, max(0, corrected)))


def hexToColor(hexa):
    hexa = hexa.replace('#', '')
    hexa = hexa.replace(' ', '')
    if(len(hexa) == 6):
        h = hexa[0:2], hexa[2:4], hexa[4:6]
    elif(len(hexa) == 3):
        h = hexa[0:1], hexa[1:2], hexa[2:3]
    else:
        return None
    return neo.Color(gamma(int(h[0], 16)), gamma(int(h[1], 16)), gamma(int(h[2], 16)))


def setColor(device, payload):
    color = hexToColor(payload)
    strip = device["strip"]
    if type(color) == type(neo.Color(0, 0, 0)):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
    device["color"] = color

def setBrightness(device, payload):
    bri = int(float(payload))
    device["strip"].setBrightness(bri)
    device["brightness"] = bri

def setState(device, payload):
    state = payload != 'false'
    device["strip"].setBrightness(device.get('brightness', 255) if state else 0)
    device["state"] = state

def ws2812b(device, msg):
    pin = int(device.get('pin'))
    prop = msg.topic.split('/')[-1]
    payload = msg.payload.decode('utf-8')
    if str(pin) not in devObj.keys():
        s = neo.Adafruit_NeoPixel(14, pin, 800000, 5, False)
        devObj[str(pin)] = {
            "strip": s,
            "color": "#000000",
            "brightness": 0,
            "state": False
        }
        s.begin()
    dev = devObj.get(str(pin))
    actions = {
        'color': setColor,
        'brightness': setBrightness,
        'state': setState
    }
    actions.get(prop, lambda d, p: None)(dev, payload)
    dev["strip"].show()


def call(device, msg):
    f = {
        'toggleable': toggleable,
        'ws2812b': ws2812b,
        '': lambda: None
    }
    f.get(device.get('type'), lambda d, m: None)(device, msg)