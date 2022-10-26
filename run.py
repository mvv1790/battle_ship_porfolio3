# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# Game's rules:
# X for boat position
# ' ' - vacant space
# O - miss

from random import randint

SIZE = 6

palyer_board = []

SCORE = 0

# 6 x 6 game board and ship locations
BATTLE_BOARD = [[' '] * 6 for x in range(6)]

# a hidded board that records hits and misses
DAMAGE_BOARD = [[' '] * 6 for i in range(6)]

# Letters to numbers conversion
letters_numbers = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}

# Player name input
name = input("You shall be known as: ")
print("Greetings, " + name)

# Start game message
print("The Battle Begins Admiral " + name)

# Create game board
def game_board(game):
    """
    Defines the board of the game
    Prints letters and the upper border of the game field
    """
    
    print('   a b c d e f')
    print('  -------------')
    row_number = 1
    for row in game:
        print(row_number,'|' + '|'.join(row) + '|')
        row_number += 1



def create_battleship(board):
    """
    Creates 7 battle ships on the board
    """
    for boat in range(7):
        boat_row, boat_column = randint(0, 5), randint(0, 5)
        while board[boat_row][boat_column] == 'X':
            boat_row, boat_column = seek_battleship()
        board[boat_row][boat_column] = 'X'
            


def seek_battleship():
    """
    The loop of the game with messages depending on the input
    """
    row = input("Seek your foe's number (from 1 to 6)...")
    while row not in '123456':
        print("Wrong input!")
        row = input("Launch your attack! (numbers from 1 to 6)")
    column = input("Seek your foe's letter (from 'a' to 'f')...")
    while column not in "abcdef":
        print("Play by the rules!")
        column = input("Seek your foe's letter! (letters from 'a' to 'f')")
    return int(row) - 1, letters_numbers[column]

def damage_done(board):
    """
    Detects hits delivered to an enemy
    """
    count = 0 
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

# The rule of 7 turns, after which the game ends
turns = 7
create_battleship(BATTLE_BOARD)
while turns > 0:
    game_board(DAMAGE_BOARD)
    row, column = seek_battleship()
    if  DAMAGE_BOARD[row][column] == 'O':
        print("This target has been hit before...")
    elif BATTLE_BOARD[row][column] == "X":
        SCORE += 1 
        print("Good shot!")
        print("Your score is:", SCORE)
        DAMAGE_BOARD[row][column] = "X"
        turns -= 1
    else:
        print("Better get some goggles!")
        DAMAGE_BOARD[row][column] = "O"
        print("Your score is:", SCORE)
        turns -= 1
    if damage_done(DAMAGE_BOARD) == 4:
        print("You have won the battle" + name, "but not the war!")
        print("Your final score is: ", SCORE, "out of 7.")
        break
    if turns == 0:
        print("You have lost the battle " + name, "but not the war!")
        print("Your final score is: ", SCORE, "out of 7.")
        break   
