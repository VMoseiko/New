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


def get_random_chest(num_chest):
    chest = []
    while len(chest) < num_chest:
        new_chest = [random.randint(0, 59), random.randint(0, 14)]
        if new_chest not in chest:
            chest.append(new_chest)
    return chest


def is_on_board(x, y):
    return 0 < x < 59 and 0 < y < 59


def make_move(chests, board, x, y):
    small_distance = 100
    for cx, cy in chests:
        distance = math.sqrt((cx-x)**2 + (cy-y)**2)

        if distance < small_distance:
            small_distance = distance

    if small_distance == 0:
        chests.remove([x, y])
        return 'вы нашли сундук с сокровищами!'

    else:
        if small_distance <= 10:
            board[x, y] = str(small_distance)
            return 'сундук с сокровищами обнружен на растоянии %s от гидролокатора' % str(small_distance)
        else:
            board[x, y] = 'X'
            return 'сундук не зоны видимости гидролокатора'















print(draw_board(get_new_board()))
