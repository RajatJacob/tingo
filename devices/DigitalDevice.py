from Device import Device
import RPi.GPIO as GPIO

class DigitalDevice(Device):
	def __init__(self, pin, type, state=False):
		print("init")
		super(DigitalDevice, self).__init__(pin, type)
		GPIO.setup(self.pin, self.type)
		setState(state)

	def setState(state):
		self.state = state
		GPIO.output(self.pin, self.state)

	def getState():
		if self.type == GPIO.IN:
			self.state = GPIO.input(self.pin)
		return self.state
