#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

import datetime
name = input('What is your name? ')
age = int(input('How old are you? '))
now = datetime.datetime.now()
current_year = now.year

print('****************************')
if(age<100):
  years_to_100 = 100 - age
  year_100 = current_year + years_to_100
  print(f'{name} in {year_100} you will be 100 years old')
else:
  print(f'{name} you already have more than 100 years')