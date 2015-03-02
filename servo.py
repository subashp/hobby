#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
# follow board GPIO header numbering scheme
GPIO.setmode(GPIO.BOARD)
# header pin number 26 (GPIO7)
GPIO.setup(26,GPIO.OUT)

p = GPIO.PWM(26,50)
p.start(7.5)

try:
	while True:
		# 0 degrees
		p.ChangeDutyCycle(2.5)
		time.sleep(1)
		p.ChangeDutyCycle(5.0)
		time.sleep(1)
		# 90 degrees
		p.ChangeDutyCycle(7.5)
		time.sleep(1)
		p.ChangeDutyCycle(10.0)
		time.sleep(1)
		# 180 degrees
		p.ChangeDutyCycle(12.5)
		time.sleep(1)
		p.ChangeDutyCycle(10.0)
		time.sleep(1)
		p.ChangeDutyCycle(7.5)
		time.sleep(1)
		p.ChangeDutyCycle(5.0)
		time.sleep(1)

except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
