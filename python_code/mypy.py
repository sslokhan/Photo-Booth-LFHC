#!/usr/bin/env python
#Shehzad and Lohn
import RPi.GPIO as GPIO
import subprocess
import time

LedPin = 11    # pin11 --- led
BtnPin = 13    # pin12 --- button

def setup():
	subprocess.call(["cancel","-a","-x"])
	subprocess.call(["cupsenable","ZJ-58"])
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
	GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to make led off
def loop():
	prev_input=0
	while True:
		if (GPIO.input(BtnPin) == GPIO.LOW and (not prev_input)): # Check whether the button is pressed or not.
			print '...led on'
			GPIO.output(LedPin, GPIO.LOW)
			# led timer
			time.sleep(0.2)
			GPIO.output(LedPin, GPIO.HIGH)  
			time.sleep(0.1)
			GPIO.output(LedPin, GPIO.LOW)  
			time.sleep(0.2)
			GPIO.output(LedPin, GPIO.HIGH)  
			time.sleep(0.1)
			GPIO.output(LedPin, GPIO.LOW)  
			time.sleep(0.2)
			GPIO.output(LedPin, GPIO.HIGH)  
			time.sleep(0.1)
			GPIO.output(LedPin, GPIO.LOW)  
			time.sleep(0.2)
			GPIO.output(LedPin, GPIO.HIGH) 
			time.sleep(0.1)
			GPIO.output(LedPin, GPIO.LOW)  
			time.sleep(1)
			GPIO.output(LedPin, GPIO.HIGH)  

			#Capture image

			subprocess.call(["raspistill", "-o", "/tmp/myimage.jpg","-ev","+1.0","-ex","sports","-t", "400"])

			# Send image to printer 
			subprocess.call([ "lp" ,"-d", "zj-58" ,"-o" ,"position=top-right" ,"-o" ,"landscape" ,"-o" ,"media=Custom.58x210mm" ,"/tmp/myimage.jpg"])

		else:
			print 'led off...'
			GPIO.output(LedPin, GPIO.HIGH) # led off
			prev_input=GPIO.input(BtnPin)
			time.sleep(0.10)

def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

