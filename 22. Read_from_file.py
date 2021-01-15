# Instead of using the .txt file from above
# (or instead of, if you want the challenge),
# take this .txt file, and count how many of each “category”
# of each image there are. This text file is actually a
# list of files corresponding to the SUN database scene
# recognition database, and lists the file directory hierarchy
# for the images. Once you take a look at the first line or
# two of the file, it will be clear which part represents the
# scene category. To do this, you’re going to have to remember
# a bit about string parsing in Python 3. I talked a little bit
# about it in this post.

text = []
with open('names.txt', 'r') as open_file:
  line = open_file.readline()
  while line:
    text.append(line.strip())
    line = open_file.readline()


#creating a list to know how many categories there are
names = []
for i in text:
  if names == []:
    names.append(i)
  else: 
    for y in names:
      if (i!=y) and (i not in names):
        names.append(i)

#Creating a dictionary to know how many words of each category that file has
names_dict = {}
for i in names:
  if names_dict == {}:
    names_dict[i] = 0
  else: 
    for y in names:
      if (i!=y) and (i not in names_dict):
        names_dict[i] = 0

#Printing how many words it has
for i in text:
  for name, value in names_dict.items():
    if (name == i):
      names_dict[name] = value + 1

print('El número de palabras en categorías es: ')
for name, value in names_dict.items():
  print(f'{name} = {value}')

