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


def setColor(strip, payload):
    color = hexToColor(payload)
    if type(color) == type(neo.Color(0, 0, 0)):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)

def setBrightness(strip, payload):
    bri = int(float(payload))
    strip.setBrightness(bri)

def setState(strip, payload):
    state = payload != 'false'
    strip.setBrightness(255 if state else 0)

def ws2812b(device, msg):
    pin = int(device.get('pin'))
    prop = msg.topic.split('/')[-1]
    payload = msg.payload.decode('utf-8')
    if str(pin) not in devObj.keys():
        s = neo.Adafruit_NeoPixel(14, pin, 800000, 5, False)
        devObj[str(pin)] = s
        s.begin()
    strip = devObj.get(str(pin))
    actions = {
        'color': setColor,
        'brightness': setBrightness,
        'state': setState
    }
    actions.get(prop, lambda s, p: None)(strip, payload)
    strip.show()


def call(device, msg):
    f = {
        'toggleable': toggleable,
        'ws2812b': ws2812b,
        '': lambda: None
    }
    f.get(device.get('type'), lambda d, m: None)(device, msg)
