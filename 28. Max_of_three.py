# Implement a function that takes as input three variables, and 
# returns the largest of the three. Do this without using the Python
#  max() function!

v1 = int(input('Write down first variable: '))
v2 = int(input('Write down second variable: '))
v3 = int(input('Write down third variable: '))

if v1 < v2:
  if v2 > v3:
    print(f'The larguest is second variable: {v2}')
  else:
    print(f'The larguest is third variable: {v3}')
else:
  print(f'The larguest is first variable: {v1}')

