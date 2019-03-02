import RPi.GPIO as GPIO
from time import sleep

Motor1A= 24
Motor1B= 23
Motor1E= 25
Motor2A= 9
Motor2B= 10
Motor2E= 11

def setupMotors(msg=""):
    print msg
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)
    GPIO.setup(Motor2A,GPIO.OUT)
    GPIO.setup(Motor2B,GPIO.OUT)
    GPIO.setup(Motor2E,GPIO.OUT)

def closedownMotors():
    print "Powering down"
    GPIO.output(Motor1E, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.LOW)
    GPIO.cleanup()

def forwards(seconds, msg=""):
    print msg, " ... ", seconds , "..."
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)
    GPIO.output(Motor2E, GPIO.HIGH)
    print "... " + seconds + " second ..."
    sleep(seconds)

def backwards(seconds, msg=""):
    print msg, " ... " , seconds , "..."
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)
    GPIO.output(Motor2E, GPIO.HIGH)
    sleep(seconds)

setupMotors("setting up")
backwards(1)
closedownMotors()
