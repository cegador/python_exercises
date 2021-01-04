# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# name_1 = input('What is your name player 1?')
# name_2 = input('What is your name player 2?')

again = True

while again == True:

  player_1 = input('Player 1 select Paper as P, Rock as R or Scissors as R ')
  player_2 = input('Player 1 select Paper as P, Rock as R or Scissors as R ')

  if (player_1 == player_2):
    print('It is a tie')

  elif (player_1 == 'R'):
    if(player_2 == 'S'):
      print('Rock wins')
    else:
      print('Paper wins')

  elif (player_1 == 'S'):
    if(player_2 == 'P'):
      print('Scissors wins')
    else:
      print('Rock wins')

  elif (player_1 == 'P'):
    if(player_2 == 'R'):
      print('Paper wins')
    else:
      print('Scissors wins')
  
  decision = input('Do you want to play again? (Y/N) ')
  if(decision == 'Y'):
    again = True
  else:
    break
