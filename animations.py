import time
import sys
from neopixel import *

LED_COUNT   = 60      # Number of LED pixels.
LED_PIN     = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA     = 5       # DMA channel to use for generating signal (try 5)
#LED_BRIGHTNESS = 255  # LED Brightness
LED_INVERT  = False   # True to invert the signal (when using NPN transistor level shift)

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)
strip.begin()

def colorWipe(arg):
	"""Wipe color across display a pixel at a time."""
	arg = arg.split(",")
	if(len(arg) < 2):
		arg.append(50)
	color = hexToArray(arg[0])
	color[0] = (color[0])/6
	color[1] = (color[1])/5
	color[2] = (color[2])/4
	color = ArrayToHex(color)
	color = hexToColor(color)
	for i in range(strip.numPixels()):
		strip.setPixelColor(LED_COUNT/2-i, color)
		strip.setPixelColor(LED_COUNT/2+1+i, color)
		strip.show()
		time.sleep(int(arg[1])/1000.0)

def fadeColor(arg):
	arg = arg.split(",")
	if(len(arg) < 2):
		arg.append(0)
	if(len(arg) < 3):
		arg.append(0)
	a=hexToArray(arg[0])
	b=hexToArray(arg[1])
	d=[True, True, True]
	wait=int(arg[2])
	while a!=b:
		for i in range(0, len(a)):
			if a[i]==b[i]:
				d[i] = False
			if (a[i] < b[i]) and d[i]:
				a[i] = a[i] + 1
			if (a[i] > b[i]) and d[i]:
				a[i] = a[i] - 1
		print str(a)+ArrayToHex(a)
		colorWipe(ArrayToHex(a)+",0")
		time.sleep(wait/1000.0)
	return 'Done.\n'

def sunrise(wait):
	wait = int(wait)
	fadeColor("000000,FF0000,"+str(wait))
	fadeColor("FF0000,FFFF00,"+str(wait))
	return 'Done.\n'

def hexToColor(hexa):
	hexa=hexa.replace('#', '')
	hexa=hexa.replace(' ', '')
	if(len(hexa)==6):
		h = hexa[0:2], hexa[2:4], hexa[4:6]
	elif(len(hexa)==3):
		h = hexa[0:1], hexa[1:2], hexa[2:3]
	else:
		return Color(int(hexa, 16), int(hexa, 16), int(hexa, 16))
	return Color(int(h[1], 16), int(h[0], 16), int(h[2], 16))

def hexToArray(hexa):
	hexa=hexa.replace('#', '')
	hexa=hexa.replace(' ', '')
	hexa=hexa.replace("0x", "")
	if(len(hexa)==6):
		h = hexa[0:2], hexa[2:4], hexa[4:6]
	elif(len(hexa)==3):
		h = hexa[0:1], hexa[1:2], hexa[2:3]
	else:
		return [int(hexa, 16), int(hexa, 16), int(hexa, 16)]
	return [int(h[0], 16), int(h[1], 16), int(h[2], 16)]

def ArrayToHex(arr):
	hexa=""
	x=""
	for i in range(0, len(arr)):
		x = str(hex(arr[i]))
		x = x.replace("0x", "")
		if(len(x)<2):
			x = "0" + x
		hexa = hexa + x
	return hexa

#if(sys.argv[1]=="colorWipe"):
#	colorWipe(sys.argv[2], int(sys.argv[3]))
#elif(sys.argv[1]=="fadeColor"):
#	fadeColor(sys.argv[2], sys.argv[3], int(sys.argv[4]))
#elif(sys.argv[1]=="sunrise"):
#	sunrise(int(sys.argv[2]))
