# In the previous exercise we created a dictionary of famous 
# scientists’ birthdays. In this exercise, modify your program
# from Part 1 to load the birthday dictionary from a JSON file 
# on disk, rather than having the dictionary defined in the program.

# Bonus: Ask the user for another scientist’s name and birthday 
# to add to the dictionary, and update the JSON file you have on 
# disk with the scientist’s name. If you run the program multiple 
# times and keep adding new names, your JSON file should keep 
# getting bigger and bigger.

# import json

# def create_json(dict):
#   with open("names.json", "w") as f:
#       json.dump(dict, f)

# def read_json():
#   with open("names.json", "r") as f:
#     names = json.load(f)
#     return (names)

# def welcome(dict):
#   print('Welcome to the birthday dictionary. We know the birthdays of: ')
#   for i in dict.keys():
#     print(i)

# def birthday(dict):
#   name = input('Who\'s birthday do you want to look up? ')
#   for x,y in dict.items():
#     if name == x:
#       print(f'{x}\'s birthday is: {y}')

# def add_name(dict):
#   res = input('Do you know another scientist birthday? (Y/N) ')
#   if res == 'Y':
#     name = input('Write scientist\'s name: ')
#     birthday = input('Write scientist\'s bithday (DD/MM/YYYY): ')
#     dict[name] = birthday
#     print('=='*20)
#     print('Dictionary was updated')
#     create_json(dict)
#     print('=='*20)
#     print('Names in dict are now:') 
#     for x,y in dict.items():
#       print(f'{x} = {y}')
#   else:
#     print('=='*20)
#     print('Dictionary remains equal')

# if __name__ =='__main__':
#   read_json()
#   welcome(names)
#   print('=='*20)
#   birthday(names)
#   print('=='*20)
#   add_name(names)


import json

def create_json():
  with open("names.json", "r") as f:
    names = json.load(f)

  print('Welcome to the birthday dictionary. We know the birthdays of: ')
  for i in names.keys():
    print(i)
  print('=='*20)

  name = input('Who\'s birthday do you want to look up? ')
  for x,y in names.items():
    if name == x:
      print(f'{x}\'s birthday is: {y}')
  print('=='*20)

  res = input('Do you know another scientist birthday? (Y/N) ')
  if res == 'Y':
    name = input('Write scientist\'s name: ')
    birthday = input('Write scientist\'s bithday (DD/MM/YYYY): ')
    names[name] = birthday
    print('=='*20)

    print('Dictionary was updated')
    with open("names.json", "w") as f:
      json.dump(names, f)
    print('=='*20)

    print('Names in dict are now:') 
    for x,y in names.items():
      print(f'{x} = {y}')

  else:
    print('=='*20)
    print('Dictionary remains equal')

if __name__ =='__main__':
  create_json()