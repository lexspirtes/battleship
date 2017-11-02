from random import randint
from sys import exit

#initializes board
board = []
for x in range(0,5):
    board.append(["0"] * 5)

#prints board to command
def print_board(board):
  for row in board:
    print " ".join(row)

def new_board():
    board = []
    for x in range(0,5):
        board.append(["0"] * 5)
    return board
#print_board(board)

#selects place for battle ship
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

#creates a new ship
def new_ship():
    sr = random_row(board)
    sc = random_col(board)
    return (sr,sc)

def battleship():
  print
  print "Hi Jack welcome to battleship"
  print
  #generates a random row and column each game
  (ship_row, ship_col) = new_ship()
  #intializes a board each game
  board = new_board()
  print_board(board)
  for turn in range(4):
    print
    print "Turn", turn + 1
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))

    if (guess_row == ship_row and guess_col == ship_col):
      print "Congratulations! You sank my battleship!"
      print playagain()
      break
    else:
      if guess_row not in range(5) or \
        guess_col not in range(5):
        print "Oops, that's not even in the ocean."
      elif board[guess_row][guess_col] == "X":
        print( "You guessed that one already." )
      else:
        print
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
      if (turn == 3):
        print ":( Game Over"
        print playagain()
        break
      print_board(board)

def playagain():
      yon = str(raw_input("Would you like to play again?, Y or N "))
      if ((yon == "Y") or (yon == "y")):
        return battleship()
      elif ((yon == "n") or (yon == "N")):
        return "Thank you for playing, goodbye!"
      else :
        print "sorry, I didn't get that"
        playagain()

print battleship()
