#guess the word
secretWord = 'panda'
guess = ''
trials = 0

while secretWord != guess:
	guess = input('p_n_a\nenter guess: ').lower()
	trials += 1

	if trials == 3:
		print('you reach the limit!\nyou lose :(')
		break
		
if guess == secretWord:
	print('you win')


