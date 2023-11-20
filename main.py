import random


class TikTacToe:

def board(board):
    empty= """
               |              |
               |              |
               |              |
               |              |
               |              |
               |              |
               |              |
               |              |
               |              |
               |              |
_____________________________________________
               |              |
               |              |
               |              |
               |              |
               |              |
               |              |
               |              |
               |              |
               |              |
_____________________________________________
               |              |
               |              |
               |              |
               |              |
               |              |
               |              |
               |              |
               |              |
               |              |

"""

def Xsqaure(num):
    seven =  [[' ',' ',' ',' ','?','8','8','8','8','P',' ',' ',' ',' '],#0
              [' ',' ',' ',' ',' ','`','8','8','`',' ',' ',' ',' ',' '],#1
              ['','',',','_',' ',' ','8','8',' ',' ','_',',','d','8'],#2
              ['','','','','','','I','C','K','8','8','8','8','8'],#3
              ['','','~',' ',' ',' ','8','8',' ',' ',' ','~','?','8'],#4
              [' ',' ',' ',' ',' ',',','8','8','.',' ',' ',' ',' ',' '],#5
              [' ',' ',' ',' ','d','8','8','8','8','b',' ',' ',' ',' ']]#6


    if num == 1:
        iOffset = 0
        jOffset = 0
    if num == 2:
        iOffset = 0
        jOffset = 16
    if num == 3:
        iOffset = 0
        jOffset = 32
    if num == 4:
        iOffset = 9
        jOffset = 0
    if num == 5:
        iOffset = 9
        jOffset = 16
    if num == 6:
        iOffset = 9
        jOffset = 32
    if num == 7:
        iOffset = 17
        jOffset = 0
    if num == 8:
        iOffset = 17
        jOffset = 16
    if num == 9:
        iOffset = 17
        jOffset = 32

    for i in range(iOffset, iOffset + 7):
        for j in range(jOffset, jOffset + 14):
            board[i+1][j] = cross[i - iOffset][j - jOffset]


-------------------------------------
# Tic Tac Toe

# Create the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    print('-------------')
    for i in range(3):
        print('|', board[i*3], '|', board[i*3 + 1], '|', board[i*3 + 2], '|')
        print('-------------')

# Function to check for a win
def check_win(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6] == player:
        return True
    return False

# Function to play the game
def play_game():
    current_player = 'X'
    game_over = False

    while not game_over:
        print_board()
        position = int(input("Enter a position (1-9): ")) - 1

        if board[position] == ' ':
            board[position] = current_player
            if check_win(current_player):
                print_board()
                print("Player", current_player, "wins!")
                game_over = True
            elif ' ' not in board:
                print_board()
                print("It's a tie!")
                game_over = True
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("That position is already filled. Try again.")

# Start the game
play_game()
