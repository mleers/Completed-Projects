print("Welcome to hangman, you have 6 guesses to figure out the word")

def picker():
	import random
	with open('hangman_library.txt', encoding = 'utf-8') as a_file:    #uses https://github.com/first20hours/google-10000-english 
        	lines = a_file.readlines()
	return(random.choice(lines).strip())

def game(word):
	guesses_left = 6
	letters_guessed = []
	wrong_letters = []
	word = picker()
	

	empty_char = ['_' for i in range(len(word))]    #defines placeholder for each letter in chosen word
	combine = ''.join(empty_char)
	print(combine)
	print("Your word is {} letters long".format(len(combine)))
	
	while '_' in empty_char:
		letter = input("Guess a letter in the word: ")
		letter = letter.upper()
		while len(letter) > 1:					  #error handling
			print("Only enter 1 letter at a time!")	 	  #multiple entries    
			letter = input("Guess a letter in the word: ")    #
			letter = letter.upper()			          #
		while len(letter) - letter.count(' ') == 0:		  #blank entries	
			print("You can not leave blank!  Enter a letter") #
			letter = input("Guess a letter in the word: ")	  #
			letter = letter.upper()				  #
		while letter.isalpha() == False:			  #non-letter entries
			print("Only letters are allowed!")	 	  #
			letter = input("Guess a letter in the word: ")    #
			letter = letter.upper()				  #
		if letter in letters_guessed:
			letter = ''
			print("Already guessed!")
		elif letter in word:
			letters_guessed.append(letter)    #add letter to guessed bank
			for i in range(len(word)):
				if word[i] == letter:    #if guessed letter is in the word...
					empty_char[i] = letter    #replace placeholder with letter  
			print(''.join(empty_char))
			print("Letters already guessed:{} ".format(letters_guessed))
		else:
			if letter not in word:
				guesses_left -= 1
				print("Letter not in word, you have {} guesses remaining!".format(guesses_left))
				letters_guessed.append(letter)
				wrong_letters.append(letter)
				print("Letters already guessed:{} ".format(letters_guessed))
				print(''.join(empty_char))

		if len(wrong_letters) == 6:    #game ending condition
			print("You are out of guesses!\n")
			print("The word was:{} ".format(word))
			break
		if '_' not in empty_char:    #game win condition
			print("You win!")
			break

while True:    #replay game decisions
	game(picker())
	again = input("Play again? (y/n)").upper()
	while again != 'Y' and again != 'N':
		again = input("You must pick y/n").upper()
	if again == 'Y': True
	if again == 'N': False, quit()

