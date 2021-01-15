# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

import random
choice = 0
times = 0
number = random.randint(1,9)

while (choice != number and choice != 'exit') :
  number = random.randint(1,9)
  choice = int(input('Write a number to guess between 1 and 9 '))

  if(choice == 'exit'):
    break

  if (choice < number):
    print('You did too low')
  elif (choice > number):
    print('You did too high')
  else:
    print('You did right!')
    times += 1


print('You have done right {} times'.format(times))



