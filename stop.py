import RPi.GPIO as GPIO

Motor1A = 24
Motor1B = 23
Motor1E = 25
Motor2A = 9
Motor2B = 10
Motor2E = 11

GPIO.setmode(GPIO.BCM)
GPIO.setup(Motor1E, GPIO.OUT)
GPIO.setup(Motor2E, GPIO.OUT)

print "Powering Down"
GPIO.setmode(GPIO.BCM)
GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)
GPIO.setup(Motor2A, GPIO.OUT)
GPIO.setup(Motor2B, GPIO.OUT)
GPIO.setup(Motor2E, GPIO.OUT)
GPIO.output(Motor1E, GPIO.LOW)
GPIO.output(Motor2E, GPIO.LOW)
GPIO.cleanup()
