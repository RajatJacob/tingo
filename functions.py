import RPi.GPIO as gpio


def toggleable(device, payload):
    gpio.output(device['pin'], gpio.LOW if payload != b'false' else gpio.HIGH)


def call(device, payload):
    f = {
        'toggleable': toggleable(device, payload),
        '': lambda: None
    }
    f[device.get('type', '')]
