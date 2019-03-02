import sys
import RPi.GPIO as GPIO
from time import sleep
from time import time

GPIO.setmode(GPIO.BCM)

Echo = 17
Read = 27
GPIO.setup(Echo, GPIO.OUT)
GPIO.setup(Read, GPIO.IN)

def get_range():
    print "getting range"
    GPIO.output(Echo, 0)
    sleep(0.1)
    GPIO.output(Echo, 1)
    sleep(0.0001)
    GPIO.output(Echo, 0)

    while GPIO.input(Read) == 0:
        print ".",
    start = time()
    while GPIO.input(Read) == 1:
        print ":",
    stop = time()
    elapsed = stop - start
    print " got ", elapsed
    distance = elapsed * 17000
    return distance

timeLimit = 30 if len(sys.argv) < 2 else float(sys.argv[1])
startedTime = time()
print "Testing for ", timeLimit, "seconds"

while time() - startedTime < timeLimit:
    distance = get_range()
    print "distance     %.1f " % distance
    sleep(0.2)

print "Finishing..."
GPIO.cleanup()

