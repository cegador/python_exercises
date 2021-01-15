#  --- --- --- 
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- --- 
# This one is 3x3 (like in tic tac toe). Obviously, they come in 
# many other sizes (8x8 for chess, 19x19 for Go, and many more).
# Ask the user what size game board they want to draw, and draw 
# it for them to the screen.

def horizontal():
  print(' ---  '*size)

def vertical():
  print('|     '*(size+1))

if __name__ == '__main__':
  size = int(input('What is the size you want? '))
  for i in range(size):
    horizontal()
    vertical()
  horizontal()