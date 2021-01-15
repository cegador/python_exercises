# In this exercise, we will finish building Hangman. In the game 
# of Hangman, the player only has 6 incorrect guesses 
# (head, body, 2 legs, and 2 arms) before they lose the game.

import random

def getting_word():
  words = []
  with open('words.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
      words.append(line.strip())
      line = open_file.readline()
  return words

def answer(word):
  answer = []
  for x in range(len(word)):
    answer.append('_')
  return answer

def guess_letter(word, answer, times):
  if(times > 1):
    for i in word:
      letter = (input('Guess a letter: ')).upper()
      if word != answer:
        if letter != i:
          times = times - 1
          print('You did wrong')
          print(f'Your have {times} tries to guess')
          print('--'*12)
          print('--'*12)
          guess_letter(word, answer, times)

        if letter == i:
            answer[word.index(i)] = letter
            print(''.join(answer))
            print('--'*12)
            print('--'*12)

    else:
      print('You guessed the word: {}'.format(''.join(word)))

  else:
      print('You have lost :(')


if __name__ == '__main__':
  times = 6
  word = [i for i in random.choice(getting_word())]
  print('--'*12)
  print('--'*12)
  print('| Welcome to hangman! |')
  print('--'*12)
  print('--'*12)
  print(f'This word has {len(word)} letters')
  guess_letter(word, answer(word), times)

#Revisar
