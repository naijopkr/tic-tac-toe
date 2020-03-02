from functions import ( 
    choose_name, 
    enter_board_size, 
    enter_position, 
    clear, 
    check_win
)
from math import ceil

players = (choose_name(1), choose_name(2))
board_size = enter_board_size()


current_round = 0

current_player = players[0]
positions_taken = [[0]*board_size for i in range(board_size)]


while current_round < board_size**2:
    for row in positions_taken:
        print(row)

    position = enter_position(current_player, board_size)
    row = ceil(position/board_size) - 1
    col = (position - 1) % board_size

    clear()

    if positions_taken[row][col] == 0:
        positions_taken[row][col] = players.index(current_player) + 1
        if check_win(positions_taken, row, col):
            print(f'{current_player} won the game')
            break

        current_round += 1
        next_player_index = current_round % 2
        current_player = players[next_player_index]
    else:
        print('Position is taken. Try again.\n')


for row in positions_taken:
    print(row) 

print('GAME OVER!')
input()

