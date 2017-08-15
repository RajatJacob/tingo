import RPi.GPIO as GPIO

class dimmer():
	def __init__(self, args):
		args = map(int, args.replace(' ', '\0').split(','))
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		self.pins = args
		for i in self.pins:
			GPIO.setup(i, GPIO.OUT)
	def setLevel(self, n):
		n = 15-int(n)
		b = [int(d) for d in str(bin(n))[2:]]
		while len(b) < len(self.pins):
			b = [0]+b
		for i in range(0, len(self.pins)):
			GPIO.output(self.pins[i], b[i])

	def setPercentage(self, p):
		x = int((float(p)/float(100))*16)-1
		if x < 0:
			x = 0
		self.setLevel(x)

	def run(self, args):
                args = args.split(' ', 1)
                function = getattr(self, args[0])
                function(args[1])

