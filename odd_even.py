#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user
print('Digit your number')
number = int(input(''))

if(number%2 == 0):
  print('Your number is even')

else:
  print('Your number is odd')
