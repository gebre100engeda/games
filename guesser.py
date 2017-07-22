#!/usr/bin/python

min_number = 0
max_number = int(raw_input("Max number? "))
print("Think of a number between 0-%s" % max_number)
raw_input("press enter key when you think of your number")

correct = False
guesses = 0
while correct is False:
	guesses = guesses + 1 
	distance = max_number - min_number
	offset = int(distance/2)
	guess = min_number + offset

	answer = raw_input("My guess is %s. Is that 'c' (correct), 'h' (high), or 'l' (low): "% guess)

	while answer not in ['c', 'h', 'l']:
		print("ERROR: Respond with 'c' (correct), 'h' (high), or 'l' (low)")
		answer = raw_input("My guess is %s. Is that 'c' (correct), 'h' (high), or 'l' (low): "% guess)

	if answer == 'c':
		break
	if answer == 'h':
		max_number = guess
	if answer == 'l':
		min_number = guess

print("correct guess is %s"% guess)
print("Guess attempts: %s" % guesses)
