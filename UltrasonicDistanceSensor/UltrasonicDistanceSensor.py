import RPi.GPIO as GPIO
import time

class UltrasonicDistanceSensor:
	"""
	@flowerChildParameter { ref = "echo", type = "int" }
	@flowerChildParameter { ref = "trigger", type = "int" }
	"""
	def __init__(self, echo = 23, trigger = 24):
		self.GPIO_TRIGGER = trigger
		self.GPIO_ECHO = echo

	def setup(self):
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
		GPIO.setup(self.GPIO_ECHO, GPIO.IN)

	def stop(self):
		GPIO.cleanup()
		return

	def distance(self):
		GPIO.output(self.GPIO_TRIGGER, True)
		time.sleep(0.00001)
		GPIO.output(self.GPIO_TRIGGER, False)
		StartTime = time.time()
		StopTime = time.time()
		while GPIO.input(self.GPIO_ECHO) == 0:
			StartTime = time.time()
		while GPIO.input(self.GPIO_ECHO) == 1:
			StopTime = time.time()
		TimeElapsed = StopTime - StartTime
		distance = (TimeElapsed * 34300) / 2
		return distance

