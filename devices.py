import RPi.GPIO as GPIO

class Device():
	def __init__(self, pin, type=GPIO.OUT):
		print("Created Device at pin #{} of type {}".format(pin, 'in' if type==GPIO.IN else 'out' ))
		self.pin = pin
		if type not in [GPIO.IN, GPIO.OUT]:
			raise Exception("Device type should be RPi.GPIO.IN or RPi.GPIO.OUT")
		self.type = type
		GPIO.setup(self.pin, self.type)

class DigitalDevice(Device):
	def setState(self, state):
		self.state = state
		GPIO.output(self.pin, not self.state)
		return self.state

	def getState(self):
		if self.type == GPIO.IN:
			self.state = GPIO.input(self.pin)
		return self.state

	def __init__(self, pin, type, state=False):
		super().__init__(pin, type)
		self.setState(state)
