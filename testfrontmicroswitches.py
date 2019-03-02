import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN)
GPIO.setup(15, GPIO.IN)

while True:
	inputleft = GPIO.input(15)
	inputright = GPIO.input(18)
	if inputleft:
		print "Pin 15 Front Left In"
	if inputright:
		print "Pin 18 Front Right In"
	if not inputleft and not inputright:
		print "."
	sleep(0.02)

GPIO.cleanup()


