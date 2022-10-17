# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
#Game rules:
# X for boat position
# ' ' vacant space
# - miss

from random import randint
"""

"""
# 8 x 8 board, game standard
BATTLE_BOARD = [[' '] * 8 for x in range(8)]
FOE_BOARD = [[' '] * 8 for x in range(8)]

#letters to numbers conversion
letters_numbers = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}

#create game board
def game_board(game):
    """
    Defines the board of the game
    """
    print(' a b c d e f g h')
    print(' ---------------')
    row_number = 1 
    for row in game:
        print("%d|%s" % (row_number, "|".join(row)))
    #for player_row in player_board:
        #print(" ".join(player_row))



def create_battleship():
    """
    Creates 3 battle ships on the board
    """
    for boat in range(3):
        boat_row, boat_column = randint(0, 7), randint(0, 7)
        while board[boat_row][boat_column] == 'X':
            boat_row, boat_column = randint(0, b7), randint(0, 7) 
        board[boat_row][boat_column] = 'X'    


def seek_battleship():
    row = input("Launch your attack!")
    while row not in '12345678':

def damage_done():
    pass