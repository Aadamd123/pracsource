#!/usr/bin/python3
"""
Names: <Aadam De Doncker>
Student Number: <DDNAAD001>
Prac: <Prac 1>
Date: <27/07/2019>
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time
#initialise input and output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# Logic that you write

#add debounce and event detection
GPIO.add_event_detect(11, GPIO.RISING, bouncetime=200)

def main():

	if GPIO.event_detected(11): #check if button is pressed
	   	if GPIO.input(12) == 1: #check if light is on and turn light off
	      		GPIO.output(12, 0)
	      		time.sleep(0.5)
	   	else:
	      		GPIO.output(12, 1) #check if light is off and turn on
			time.sleep(0.5)

# Only run the functions if
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
