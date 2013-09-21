from random import randint

# Let's play battleship!


board = []


# Generate the 5 x 5 for battleship


for x in range(0, 5):
    board.append(["O"] * 5)


# print_board provides a human viewable grid


def print_board(board):
    for row in board:
        print " ".join(row)


# Define the functions used to generate a random row and column location.


# def random_row(board):
#    return randint(0, len(board) - 1)


def random_row(board):
    x = 0
    y = len(board) - 1
    return randint(x, y)


# def random_col(board):
#    return randint(0, len(board[0]) - 1)


def random_col(board):
    x = 0
    y = len(board[0]) - 1
    return randint(x, y)


# Generate the random location on the grid to place the battleship.


ship_row = random_row(board)
ship_col = random_col(board)

# print print_board(board)
# print random_row(board)
# print random_col(board)

# Debugging output for testing Win
# print ship_row
# print ship_col


# Setup the logic of the battleship game


def battleship():
    for turn in range(4):
        guess_row = int(raw_input('Guess Row:'))
        guess_col = int(raw_input('Guess Col:'))
        if guess_row == ship_row and guess_col == ship_col:
            print "Congratulations! You sank my battleship!"
            break

        else:
            if (guess_row < 0 or guess_row > 5) or (
                    guess_col < 0 or guess_col > 5):
                print "Oops, that's not even in the ocean."
# [cody@laptop github]$ python battleship.py 
# Guess Row:5
# Guess Col:2
# Traceback (most recent call last):
#  File "battleship.py", line 90, in <module>
#    battleship()
#  File "battleship.py", line 78, in battleship
#    elif (board[guess_row][guess_col] == "X"):
# IndexError: list index out of range
            elif (board[guess_row][guess_col] == "X"):
                print "You guessed that one already."

            else:
                print "You missed my battleship!"
                board[int(guess_row)][int(guess_col)] = "X"

            if turn == 3:
                print "Game Over"

        print print_board(board)

battleship()
