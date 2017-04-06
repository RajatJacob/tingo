import RPi.GPIO as GPIO
import time

class relay(object):
	pins = []

	def __init__(self, pins):
		self.pins = pins
		GPIO.setmode(GPIO.BCM)
		for i in pins:
			GPIO.setup(i, OUT, )

	def a(self, state):
		GPIO.output(pins[1], state)
	def b(self, state):
		GPIO.output(pins[2], state)
	def c(self, state):
		GPIO.output(pins[3], state)
	def d(self, state):
		GPIO.output(pins[4], state)
