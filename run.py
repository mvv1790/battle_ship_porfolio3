# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# Game rules:
# X for boat position
# ' ' vacant space
# - miss

from random import randint
"""

"""
# 8 x 8 board, game standard
BATTLE_BOARD = [[' '] * 6 for x in range(6)]
FOE_BOARD = [[' '] * 6 for x in range(6)]

#letters to numbers conversion
letters_numbers = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,}

#create game board
def game_board(game):
    """
    Defines the board of the game
    """
    print(' a b c d e f')
    print(' -----------')
    row_number = 1 
    for row in game:
        print("%d|%s" % (row_number, "|".join(row)))
        row_number += 1

letters_to_numbers = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5
}
    #for player_row in player_board:
        #print(" ".join(player_row))



def create_battleship(board):
    """
    Creates 3 battle ships on the board
    """
    for boat in range(3):
        boat_row, boat_column = randint(0, 5), randint(0, 5)
        while board[boat_row][boat_column] == 'X':
            boat_row, boat_column = randint(0, 5), randint(0, 5) 
        board[boat_row][boat_column] = 'X'    


def seek_battleship():
    row = input("Seek your foe's number!")
    while row not in '123456':
        print("Try again!")
        row = input("Launch your attack!")
    column = input("Seek your foe's letter!")
    while column not in "abcdef":
        print("Try again!")
        column = input("Seek your foe's letter!")
    return int(row) - 1, letters_numbers[column]

def damage_done(board):
    count = 0 
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

    

create_battleship(BATTLE_BOARD)
game_board(BATTLE_BOARD)
game_board(FOE_BOARD)
turns = 10
#while turn > 0:
