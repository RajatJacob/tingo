import RPi.GPIO as GPIO

# Device

class Device():
	def __init__(self, name, pin, type=GPIO.OUT):
		print("Created Device '{}' at pin #{} of type {}".format(name, pin, 'in' if type==GPIO.IN else 'out' ))
		self.name = name
		self.pin = pin
		if type not in [GPIO.IN, GPIO.OUT]:
			raise Exception("Device type should be RPi.GPIO.IN or RPi.GPIO.OUT")
		self.type = type
		GPIO.setup(self.pin, self.type)

	def __str__(self):
		return "[{} @ #{}]: {}".format(self.name, self.pin, self.state)

	def __repr__(self):
		return self.__str__()

# DigitalDevice

class DigitalDevice(Device):
	def __init__(self, name, pin, type, state=False, setState=True):
		super().__init__(name, pin, type)
		if setState:
			self.setState(state)

	def setState(self, state):
		if type(state) is not type(True):
			state = state == b'true' or state == 1 or state == "true"
		self.state = state
		print(self)
		GPIO.output(self.pin, not self.state)
		return self.state

	def getState(self):
		if self.type == GPIO.IN:
			self.state = GPIO.input(self.pin)
		return self.state
