import RPi.GPIO as GPIO

class Device():
	def __init__(self, pin, type=GPIO.OUT):
		self.pin = pin
		if type not in [GPIO.IN, GPIO.OUT]:
			raise Exception("Device type should be RPi.GPIO.IN or RPi.GPIO.OUT")
			self.type = type

class DigitalDevice(Device):
	def __init__(self, pin, type, state=False):
		super(DigitalDevice, self).__init__(pin, type)
		GPIO.setup(self.pin, self.type)
		setState(state)

	def setState(self, state):
		self.state = state
		GPIO.output(self.pin, self.state)

	def getState(self):
		if self.type == GPIO.IN:
			self.state = GPIO.input(self.pin)
		return self.state
