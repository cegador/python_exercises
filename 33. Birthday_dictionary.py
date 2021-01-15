# For this exercise, we will keep track of when our friend’s birthdays
#  are, and be able to find that information based on their name. 
#  Create a dictionary (in your file) of names and birthdays. 
#  When you run your program it should ask the user to enter a name, 
#  and return the birthday of that person back to them. 
import json

dict = {
  'Luis': '05/04/1994',
  'Lina': '12/07/1987'
}

def create_json(dict):
  with open("names.json", "w") as f:
    json.dump(dict, f)

def welcome():
  print('Welcome to the birthday dictionary. We know the birthdays of: ')
  for i in dict.keys():
    print(i)

def birthday():
  name = input('Who\'s birthday do you want to look up? ')
  for x,y in dict.items():
    if name == x:
      print(f'{x}\'s birthday is: {y}')

if __name__ == '__main__':
  welcome()
  birthday()
  create_json(dict)


