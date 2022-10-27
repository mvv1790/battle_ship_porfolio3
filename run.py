"""The Battel Ship Game"""
# Game's rules
# ' ' -  space
# X - hit
# O - miss

from random import randint


SCORE = 0
SOCRE_AI = 0
BOAT_LENGTH = [2, 3, 4]

# 6 x 6 game board and ship locations
BATTLE_BOARD = [[' '] * 6 for x in range(6)]
BATTLE_BOARD_AI = [[' '] * 6 for x in range(6)]

# a hidded board that records hits and misses
DAMAGE_BOARD = [[' '] * 6 for i in range(6)]
DAMAGE_BOARD_AI = [[' '] * 6 for x in range(6)]

# Letters to numbers conversion
letters_numbers = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}


# Player name input
try:
    print("---------------------------------")
    name = input("You shall be known as: ")
    print("---------------------------------")
    print("Greetings, " + name, ". There\nare seven enemy ships,")
    print("destroy at least three of them\nto win the battle before")
    print("the 7th turn.")
    print("---------------------------------")
except EOFError as e:
    print(e)
# Start game message
try:
    print("The Battle Begins Admiral " + name)
    print("---------------------------------")
except EOFError as e:
    print(e)


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
        print(row_number, '|' + '|'.join(row) + '|')
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
    The messages that appear depending on the input
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


TURNS = 7


create_battleship(BATTLE_BOARD)
print(BATTLE_BOARD)


while TURNS > 0:
    game_board(DAMAGE_BOARD)
    row, column = seek_battleship()
    if DAMAGE_BOARD[row][column] == 'O':
        print("----------------------------------")
        print("This target has been hit before...")
        print("----------------------------------")
        print("Computer hits the same target")
    elif BATTLE_BOARD[row][column] == "X":
        SCORE += 1
        SOCRE_AI -= 1
        print("----------")
        print("Good shot!")
        print("---------------------")
        print(name + " your score is:", SCORE)
        print("Computer score is:", SOCRE_AI)
        print("---------------------")
        DAMAGE_BOARD[row][column] = "X"
        TURNS -= 1
    else:
        print("------------------------")
        print("Better get some goggles!")
        print("------------------------")
        DAMAGE_BOARD[row][column] = "O"
        print("---------------------")
        print(name + " your score is:", SCORE)
        print("Computer score is:", SOCRE_AI)
        print("---------------------")
        TURNS -= 1
        SOCRE_AI += 1
    if damage_done(DAMAGE_BOARD) == 3:
        print("--------------------------------------------------")
        print("You have won the battle " + name, "but not the war!")
        print("Your final score is: ", SCORE, "out of 7.")
        print("--------------------------------------------------")
        break
    if TURNS == 0:
        print("--------------------------------------------------")
        print("You have lost the battle " + name, "but not the war!")
        print("Your final score is:", SCORE, "out of 7.")
        print("--------------------------------------------------")
        break
