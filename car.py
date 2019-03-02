import sys
import RPi.GPIO as GPIO
from time import sleep
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
GPIO.setup(15, GPIO.IN)

Motor1A = 24
Motor1B = 23
Motor1E = 25
Motor2A = 9
Motor2B = 10
Motor2E = 11


def setupMotors(msg=""):
    print msg
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Motor1A, GPIO.OUT)
    GPIO.setup(Motor1B, GPIO.OUT)
    GPIO.setup(Motor1E, GPIO.OUT)
    GPIO.setup(Motor2A, GPIO.OUT)
    GPIO.setup(Motor2B, GPIO.OUT)
    GPIO.setup(Motor2E, GPIO.OUT)


def stop():
    GPIO.output(Motor1E, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.LOW)


def closedownMotors(msg=""):
    print msg
    stop()
    GPIO.cleanup()


def forwards(seconds, msg=""):
    print msg + " ... ", seconds, "..."
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)
    GPIO.output(Motor2E, GPIO.HIGH)
    sleep(seconds)


def backwards(seconds, msg=""):
    print msg + " ... ", seconds, "..."
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)
    GPIO.output(Motor2E, GPIO.HIGH)
    sleep(seconds)


def left(seconds, msg=""):
    print msg + " ... ", seconds, "..."
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)

    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)
    sleep(seconds)


def right(seconds, msg=""):
    print msg + " ... ", seconds, "..."
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)

    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)
    GPIO.output(Motor2E, GPIO.HIGH)
    sleep(seconds)


setupMotors("setting up")

timeLimit = 10 if len(sys.argv) < 2 else float(sys.argv[1])
startedTime = time.time()

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
