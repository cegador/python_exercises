#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

print('Text your number: ')
number = int(input(''))
numbers = []
divisors = []

for i in range(1,number+1):
  numbers.append(i)

for y in numbers:
  if(number%y == 0):
    divisors.append(y)


print('{} has the following divisors: {}'.format(number, divisors))