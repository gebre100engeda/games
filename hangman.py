#!/usr/bin/python

#  $ ./hangman.py
#  Your word: _______
#  Letter? S
#  Your word: __SS__S
#  Letter? X
#  WRONG! You have 1 guesses left
#  Your word: __SS__S
#  Letter? E
#  Your word: _ESS__S
#  Letter? E
#  Your word: _ESS__S
#  Letter? L
#  Your word: LESS__S
#  Letter? Q
#  WRONG! You have 0 guesses left
#  You lose!

def print_word(word, letters):
	''' Print word with unguessed letters substituted with "_"
	'''
	partial_word = ''
	for letter in word:
		if letter.upper() in [l.upper() for l in letters]:
			partial_word = partial_word + letter
		else:
			partial_word = partial_word + '_'
	print('Your word: %s' % partial_word)


def word_is_guessed(word, letters):
	''' Return True if entire word guessed
	'''
	if set(word).issubset(set([l.upper() for l in letters])):
		return True
	else:
		return False

word = "LESSONS"
guesses = 10
letters = []

while True:
	print_word(word, letters)

	# Ask for letter guess
	guess = raw_input("Guess a letter A - Z: " ) 
	letters.append(guess)

	if guess.upper() not in word:
		guesses -= 1 
		print("Wrong! You have %s guesses left" % guesses )
	if guesses == 0:
		print("Thanks for playing")
		break
	if word_is_guessed(word, letters):
		print_word(word, letters)
		print("Well Done!")
		break
	
