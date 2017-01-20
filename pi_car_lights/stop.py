"""
"""
import RPi.GPIO as GPIO
import time

LIGHT_PIN = 5

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(LIGHT_PIN, GPIO.OUT)

print "LED on"
GPIO.output(LIGHT_PIN, GPIO.HIGH)

time.sleep(1)

print "LED off"
GPIO.output(LIGHT_PIN, GPIO.LOW)
