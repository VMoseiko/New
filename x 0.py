import random


def print_board(board):
    # печатаем доску, с разделителями
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def player_letter():
    letter = ''
    # выбираем букву, возвращает словарь у нас выбранная буква у ИИ - другая
    while not (letter == 'X' or letter == 'O'):
        print('Выберите "Х" или "О"')
        letter = input().upper()
    if letter == 'X':
        return {'player': 'X', 'AI': 'O'}
    else:
        return {'player': 'O', 'AI': 'X'}


def who_goes():
    # кто ходит первым
    if random.randint(0, 1) == 0:
        return 'AI'
    else:
        return 'player'


def make_move(board, letter, move):
    board[move] = letter
    return board


#     делаем ход

def is_winner(board, letter):
    # условия победы

    return (board[7] == letter and board[8] == letter and board[9] == letter) or (
            board[4] == letter and board[5] == letter and board[6] == letter) or (
            board[1] == letter and board[2] == letter and board[3] == letter) or (
            board[7] == letter and board[4] == letter and board[1] == letter) or (
            board[8] == letter and board[5] == letter and board[2] == letter) or (
            board[9] == letter and board[6] == letter and board[3] == letter) or (
            board[7] == letter and board[5] == letter and board[3] == letter) or (
            board[1] == letter and board[5] == letter and board[9] == letter)


def is_free(board, move):
    if board[move] == ' ':
        return move
    # свободна ли клетка


def get_player_move(board):
    # ход игрока
    # вызывается до тех пор пока не выберет пустую клетку
    move = ' '
    while move not in board.keys() or not is_free(board, move):
        print('Ваш следующий ход 1-9')
        move = int(input())
    return move


def choose_random_move_from_list(board, move_list):
    # проверка допустимых ходов из предлогаемого списка, выбор случайного из них для ИИ
    possible_move = []
    for i in move_list:
        possible_move.append(is_free(board, i))

    if possible_move != []:
        return random.choice(possible_move)
    else:
        return None


def get_ai_move(board, players_letter):
    for i in range(1, 10):
        the_board_copy = board.copy()
        if is_free(the_board_copy, i):
            make_move(the_board_copy, players_letter['AI'], i)
            # пробная комбинация доски
            if is_winner(the_board_copy, players_letter['AI']):
                # если комбинация выиграшная, возвращает выбранный ход
                return i

    # проверяем выигает ли игрок сделав следующий ход? если да, ИИ блокирует его
    for i in range(1, 10):
        the_board_copy = board.copy()
        if is_free(the_board_copy, i):
            make_move(the_board_copy, players_letter['player'], i)
            # пробная комбинация доски
            if is_winner(the_board_copy, players_letter['player']):
                # если комбинация выиграшная, возвращает выбранный ход
                return i
    # если выигашных ходов нет, выбираем куда ИИ идет далее

    # центр
    if is_free(board, 5):
        return 5

    # углы
    moves = choose_random_move_from_list(board, [1, 3, 7, 9])
    if moves is not None:
        return moves

    # остальное
    return choose_random_move_from_list(board, [2, 4, 6, 8])


def is_board_fool(board):
    # если занят - тру
    for i in range(1, 10):
        if is_free(board, i):
            return False
    else:
        return True


# присутпаем к сборке
print('Игра крестики - нолики')

while True:
    the_board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    players_letter = player_letter()
    turn = who_goes()
    print(turn + ' ходит первым')

    while True:
        if turn == 'player':
            print_board(the_board)
            move = get_player_move(the_board)
            make_move(the_board, players_letter['player'], move)

            if is_winner(the_board, players_letter['player']):
                print_board(the_board)
                print('Вы выиграли!')
                break
            else:
                if is_board_fool(the_board):
                    print_board(the_board)
                    print('Ничья!')
                    break
                else:
                    turn = 'AI'
        else:
            move = get_ai_move(the_board, players_letter)
            make_move(the_board, players_letter['AI'], move)

            if is_winner(the_board, players_letter['AI']):
                print_board(the_board)
                print('Вы проиграли!')
                break
            else:
                if is_board_fool(the_board):
                    print_board(the_board)
                    print('Ничья!')
                    break
                else:
                    turn = 'player'
