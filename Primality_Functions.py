# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.

def prime (number):
  divisors = []
  if (number == 1):
    print('{} is prime'.format(number))
  elif(number == 2):
    print('{} is prime'.format(number))

  divisors = [i for i in range(2,number)if(number % i == 0)]
  
  if (len(divisors) == 0):
    print('{} is prime'.format(number))
  else:
    print('{} is not prime'.format(number))



number = int(input('Write a number to know if it is a prime '))
prime(number)