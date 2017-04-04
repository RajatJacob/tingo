import time
import sys
from neopixel import *

LED_COUNT   = 48      # Number of LED pixels.
LED_PIN     = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA     = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255  # LED Brightness
LED_INVERT  = False   # True to invert the signal (when using NPN transistor level shift)

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)
strip.begin()

#Gamma correction: https://learn.adafruit.com/led-tricks-gamma-correction/the-quick-fix
gamma = [
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,
    1,  1,  1,  1,  1,  1,  1,  1,  1,  2,  2,  2,  2,  2,  2,  2,
    2,  3,  3,  3,  3,  3,  3,  3,  4,  4,  4,  4,  4,  5,  5,  5,
    5,  6,  6,  6,  6,  7,  7,  7,  7,  8,  8,  8,  9,  9,  9, 10,
   10, 10, 11, 11, 11, 12, 12, 13, 13, 13, 14, 14, 15, 15, 16, 16,
   17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 24, 24, 25,
   25, 26, 27, 27, 28, 29, 29, 30, 31, 32, 32, 33, 34, 35, 35, 36,
   37, 38, 39, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50,
   51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 66, 67, 68,
   69, 70, 72, 73, 74, 75, 77, 78, 79, 81, 82, 83, 85, 86, 87, 89,
   90, 92, 93, 95, 96, 98, 99,101,102,104,105,107,109,110,112,114,
  115,117,119,120,122,124,126,127,129,131,133,135,137,138,140,142,
  144,146,148,150,152,154,156,158,160,162,164,167,169,171,173,175,
  177,180,182,184,186,189,191,193,196,198,200,203,205,208,210,213,
  215,218,220,223,225,228,231,233,236,239,241,244,247,249,252,255] 

def colorWipe(arg):
	"""Wipe color across display a pixel at a time."""
	arg = arg.split(",")
	if(len(arg) < 2):
		arg.append("50")
	color = hexToArray(arg[0])
	color[0] = gamma[color[0]]
	color[1] = gamma[color[1]]
	color[2] = gamma[color[2]]
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
	wait=arg[2]
	while a!=b:
		for i in range(0, len(a)):
			if a[i]==b[i]:
				d[i] = False
			if (a[i] < b[i]) and d[i]:
				a[i] = a[i] + 1
			if (a[i] > b[i]) and d[i]:
				a[i] = a[i] - 1
		#print str(a)+ArrayToHex(a)
		colorWipe(ArrayToHex(a)+","+wait)
	return 'Done.\n'

def sunrise(wait):
	fadeColor("000000,550000,"+str(wait))
	fadeColor("550000,FFC000,"+str(wait))
	fadeColor("FFC000,FFFF00,"+str(wait))
	fadeColor("FFFF00,FFFFFF,"+str(wait))
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
		