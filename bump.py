import sys
import RPi.GPIO as GPIO
import time
from car import forwards, backwards, left, right, closedownMotors, setupMotors

timeLimit = 30 if len(sys.argv) < 2 else float(sys.argv[1])
startedTime = time.time()

setupMotors()

while time.time() - startedTime < timeLimit:
    hitLeft = GPIO.input(15)
    hitRight = GPIO.input(18)
    if hitLeft and hitRight:
        print(" hit front "),
        backwards(3)
        right(2)
    elif hitLeft:
        print(" hit left "),
        backwards(1)
        right(2)
    elif hitRight:
        print(" hit right "),
        backwards(1)
        left(2)
    else:
        print(".No hits."),
        forwards(0.3)

closedownMotors("Powering down")
