import random

words = []

def getting_text():
  with open('words.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
      words.append(line.strip())
      line = open_file.readline()

def random_word():
  word = random.choice(words)
  return word

if __name__ == '__main__':
  getting_text()
  print(f'A random word is {random_word()}')
  