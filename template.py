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

#setup and initialise GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# Logic and code

#initialise global counter
c = -1

#Function to count up until 7 and then reset to 0
def countUp():
	global c
	if c < 7:
	   c += 1
	   return c
	else:
	   c = 0
	   return c

#Function to count down to 0 and reset to 7
def countDown():
	global c
	if c > 0:
	   c -= 1
	   return c
	else:
	   c = 7
	   return c

#Event detector with debounce for count up button
def my_callback1(channel):
	print('button pressed')

GPIO.add_event_detect(11, GPIO.RISING, callback=my_callback1, bouncetime=200)

#Event detector with debounce for count down button
def my_callback2(channel):
	print('button pressed')

GPIO.add_event_detect(13, GPIO.RISING, callback=my_callback2, bouncetime=200)

#main function
def main():

	if GPIO.event_detected(11): #check if countUp button (pin 11) is pressed
 	   countUp() #countUp function
	   arr = [int(i) for i in bin(c)[2:]] #convert number from countUp to binary array
	   arr.reverse() #reverse array
	   while len(arr) < 3: #loop to keep array length of 3
	         arr.append(0)
	   print (arr)
	   for x in range(len(arr)): #convert each bit of the binary array to output command
	       if x == 0:
		  GPIO.output(12, arr[x])
	       if x == 1:
		  GPIO.output(16, arr[x])
	       if x == 2:
		  GPIO.output(18, arr[x])

	if GPIO.event_detected(13): #check if countDown button (pin 13) is pressed
 	   countDown() #countDown function
	   arr = [int(i) for i in bin(c)[2:]] #convert number to binary array
	   arr.reverse() #reverse array
	   while len(arr) < 3: #keep array length 3
	         arr.append(0)
	   print (arr)
	   for x in range(len(arr)): #convert each bit of the binary array to output command
	       if x == 0:
	          GPIO.output(12, arr[x])
	       if x == 1:
		  GPIO.output(16, arr[x])
	       if x == 2:
	          GPIO.output(18, arr[x])

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
