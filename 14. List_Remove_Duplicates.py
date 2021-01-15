# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

def main():
  a = [1, 1, 2, 3, 2, 3, 4, 5, 6, 7]
  # b = [i for i in a for y in b if y not in a]
  b = a.copy()
  c = []
  for i in a:
    for y in b:
      if (y == i and y not in c):
        c.append(y)
        
  print(c)

def sett():
  a = [1, 1, 2, 3, 2, 3, 4, 5, 6, 7]
  a = set(a)
  print(a)

sett()

