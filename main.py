import random

# Define the size of the game board
ROWS = 5
COLS = 5

# Define the number of mines
MINES = 3

# Create the game board
board = [[0 for j in range(COLS)] for i in range(ROWS)]

# Place the mines randomly on the board
for i in range(MINES):
  row = random.randint(0, ROWS - 1)
  col = random.randint(0, COLS - 1)
  board[row][col] = "*"


# Define a function to print the board
def print_board(board):
  for row in board:
    print(" ".join(str(cell) for cell in row))


# Define a function to get the user's guess
def get_guess():
  row = int(input("Guess row (0-4): "))
  col = int(input("Guess col (0-4): "))
  return row, col


# Define a function to check if the guess is correct
def is_correct_guess(row, col):
  if board[row][col] == "*":
    print("You hit a mine!")
    return True
  else:
    print("You missed!")
    return False


# Play the game
print("Welcome to Minefield!")
print("There are", MINES, "mines hidden on the board.")
print_board(board)

while True:
  row, col = get_guess()
  if is_correct_guess(row, col):
    break

print_board(board)
print("Game over!")
