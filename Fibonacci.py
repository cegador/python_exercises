# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.

def Fibonnaci(number):
  x = [1, 1]
  z = 2
  if(number == 1):
    print('For that number Fibonnaci serie is: [1]')
  elif(number == 2):
    print('For that number Fibonnaci serie is: [1, 1]')
  else:
    while (z < number):
      b = x[len(x)-1] + x[len(x)-2]
      x.append(b)
      z += 1
    print('For that number Fibonnaci serie is: {}'.format(x))
  

a = int(input('Write how many numbers of Fibonacci serie you want to see '))
Fibonnaci(a)