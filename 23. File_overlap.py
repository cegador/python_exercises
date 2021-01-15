# Given two .txt files that have lists of numbers in them, find 
# the numbers that are overlapping. One .txt file has a list of all 
# prime numbers under 1000, and the other .txt file has a list of 
# happy numbers up to 1000.

one = []
two = []

def open_files():

  with open('one.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
      one.append(line.strip())
      line = open_file.readline()


  with open('two.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
      two.append(line.strip())
      line = open_file.readline()

if __name__ == '__main__':
  common = []
  open_files()
  common = [i for i in one for y in two if(y == i and y not in common)]
  print(f'First list: ', one)
  print('='*70)
  print(f'Second list: ', two)
  print('='*70)
  print(f'Overlap list: ', common)


