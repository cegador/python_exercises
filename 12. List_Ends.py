# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
import random

def list_gen(numbers):
  a =[]

  for i in range(0,numbers):
    b = random.randint(1,100)
    a.append(b)

  print('This is the original list {}'.format(a))

  del a[1:(len(a)-1)]

  print('This is the new list {}'.format(a))


numbers = int(input('Write lengh list extension number'))

list_gen(numbers)




