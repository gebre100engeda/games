#!/usr/bin/python

import sys
import random


max_number = 100000000
num = int(random.randint(0, max_number))

guesses = 0
while True:
	
	guess = int(raw_input("Guess a number 0 - %s: " % max_number))
	guesses += 1
	if guess == num:
		print("Correct!")
		break
	if guess > num:
		print("Too high")
	if guess < num:
		print("Too low")

print("Total guesses: %s" % guesses)
