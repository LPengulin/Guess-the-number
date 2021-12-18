"""
Simple python number guessing game from "The Big Book of Small Python Projects"
"""


import random

max_digits = 3
max_turns = 10


def get_num():
	numbers = list('0123456789')
	random.shuffle(numbers)
	random_num = ''
	for i in range(max_digits):
		random_num += str(numbers[i])
	return random_num


def get_hint(guess, random_number):
	if guess == random_number:
		return 'You got it!'
	clues = []

	for i in range(len(guess)):
		if guess[i] == random_number[i]:
			clues.append('Yippee')
		elif guess[i] in random_number:
			clues.append('Chirp')

	if len(clues) == 0:
		return 'Doodoo'
	else:
		clues.sort()
		return ''.join(clues)

def main():
	print(f"Guess the {max_digits} digit number:")
	print(''' I will define a dictionary of clues 
Yippee : One digit correct as well as in the right position
Chirp : One digit correct however in the wrong position
Doodoo : No digits are correct

''')
	
	while True:
		target_num = get_num()
		print(f"You have {max_turns} chances to get it right.")
		
		turn_count = 1
		while turn_count <= max_turns:
			guess = ''
			while len(guess) != max_digits or not guess.isdecimal():
				print(f"Guess {turn_count}: ")
				guess = input("==> ")
				
			clues = get_hint(guess, target_num)
			print(clues)
			turn_count += 1

			if guess == target_num:
				break

			if turn_count > max_turns:
				print('You ran out of guesses.')
				print(f'The answer was {target_num}')

			
		print('Try again? (Y/N) ')
		if not input('==> ').lower().startswith('y'):
			break



if __name__ == '__main__':
	main()




