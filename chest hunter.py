import sys
import math
import random

def get_new_board():
    # создаем игровое поле размером 60*15 , со случайными волнами
    board = []
    for x in range(60):
        board.append([])
        # список из 60 списков (ячейки в  строке)
        for y in range(15):
            if random.randint(0, 1) == 1:
                board[x].append('~')
            else:
                board[x].append('`')

    return board


def draw_board(board):
    tens_distance_line = ' '
    for i in range(1, 6):
        tens_distance_line += (' ' * 9) + str(i)
    print('  ' + tens_distance_line)
    print('  ' + '0123456789' * 6)
    print()

    for row in range(15):
        if row < 10:
            extra_space = ' '
        else:
            extra_space = ''
        board_row = ''
        for column in range(60):
            board_row += board[column][row]

        # превращаем в строку %s , экранируем символы, делаем по шаблону '%s%s %s %s'
        print('%s%s %s %s' % (extra_space, row, board_row, row))
    print('  ' + tens_distance_line)
    print('  ' + '0123456789' * 6)
    print()






print(draw_board(get_new_board()))
