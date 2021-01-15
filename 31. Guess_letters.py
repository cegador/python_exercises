# Let’s say the word the player has to guess is “EVAPORATE”.
# For this exercise, write the logic that asks a player to guess
# a letter and displays letters in the clue word that were guessed
# correctly. For now, let the player guess an infinite number of
# times until they get the entire word. As a bonus, keep track of
# the letters the player guessed and display a different message if
# the player tries to guess that letter again. Remember to stop the
# game when all the letters have been guessed correctly! Don’t worry
# about choosing a word randomly or keeping track of the number of
# guesses the player has remaining - we will deal with those in a
# future exercise.

def guess_letter(word, answer):
  for i in word:
    letter = input('Guess a letter: ')
    if word != answer:
      if letter != i:
        print('You did wrong')
        print('--'*12)
        print('--'*12)
        guess_letter(word, answer)

      if letter == i:
          answer[word.index(i)] = letter
          print(''.join(answer))
          print('--'*12)
          print('--'*12)

  print('You guessed the word: {}'.format(''.join(word)))





if __name__ == '__main__':

  word = ['e','v','a']
  answer = []
  for x in range(len(word)):
    answer.append('_')


  print('--'*12)
  print('--'*12)
  print('| Welcome to hangman! |')
  print('--'*12)
  print('--'*12)
  print(f'This word has {len(word)} letters')
  guess_letter(word, answer)

#Check de letras repetidas


