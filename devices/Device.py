import RPi.GPIO as GPIO

class Device():
	def __init__(self, pin, type=GPIO.OUT):
		self.pin = pin
		if type not in [GPIO.IN, GPIO.OUT]:
			raise Exception("Device type should be RPi.GPIO.IN or RPi.GPIO.OUT")
			self.type = type
