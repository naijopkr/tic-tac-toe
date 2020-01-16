from sys import exit, platform
from os import system

def clear():
    if platform == 'win32':
        system('cls')
    else:
        system('clear')

def choose_name(player):
    return input(f'Hello, enter the name for player {player}: ')

def enter_position(player, board_size):
    while True:
        try:
            position_str = input(f'{player}, enter a number from 1 to {board_size**2}: ')
            if position_str == 'q':
                exit(0)

            position = int(position_str)
            if position in range(1, board_size**2 + 1):
                break
        except ValueError:
            pass
        
        print('Invalid position, try again.')
    
    return position


def enter_board_size():
    while True:
        try:
            board_size = int(input('Enter the board size (min. 3): '))
            if (board_size >= 3):
                break
        except:
            pass

        print('Invalid size, try another.')

    return board_size


def check_win(positions_taken, row_taken, col_taken):
    last_index = len(positions_taken) - 1
    row_win = len(set(positions_taken[row_taken])) == 1
    col_win = len(set(row[col_taken] for row in positions_taken)) == 1
    
    diagonal_win = False
    anti_diagonal_win = False

    if row_taken + col_taken == last_index or row_taken == col_taken:
        diagonal = set()
        anti_diagonal = set()
        for index in range(len(positions_taken)):
            row = positions_taken[index]
            index_anti = last_index - index
            diagonal.add(row[index])
            anti_diagonal.add(row[len(row) - 1 - index])
        diagonal_win = len(diagonal) == 1 and min(diagonal) != 0
        anti_diagonal_win = len(anti_diagonal) == 1 and min(anti_diagonal) != 0

    return row_win or col_win or diagonal_win or anti_diagonal_win