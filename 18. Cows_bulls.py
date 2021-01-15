# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have.

number = [input('Welcome to cows and bulls. First write a number o 4 digits: ')]
print('For every digit that the you guess correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.”')

import random
numbers = [0,1,2,3,4,5,6,7,8,9]
num = [random.choice(numbers) for i in range(0,4)]
numbe = [int([i]) for i in (number)]

print(numbe)



