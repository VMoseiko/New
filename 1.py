grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

y = 0
for i in range(len(grid)):
    if y <= len(grid[i]) - 1:
        x = 0
        for a in range(len(grid)):
            print(grid[x][y], end=' ')
            x += 1
        print('')
        y += 1


spam = ['apples', 'banans', 'tofu', 2, 3.14, 'cat']
# print(spam)
new_string =''
for i in spam[0:-1]:

    new_string += str(i)+ ', '
new_string += 'and '+ spam[-1]
print(new_string)

the_board = {'top_L': ' ', 'top_M': ' ', 'top_R': ' ',
             'mid_L': ' ', 'mid_M': ' ', 'mid_R': ' ',
             'low_L': ' ', 'low_M': ' ', 'low_R': ' '}


def print_board(board):
    print(board['top_L'] + '|' + board['top_M'] + '|' + board['top_R'])
    print('-+-+-')
    print(board['mid_L'] + '|' + board['mid_M'] + '|' + board['mid_R'])
    print('-+-+-')
    print(board['low_L'] + '|' + board['low_M'] + '|' + board['low_R'])




stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(inventory):
    print('Inventory: ')
    total_item = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total_item += v
    print('Total number in items:' + str(total_item))


dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'gold coin', 'bow']


def string_to_dict(string):
    new_dict = {}
    for i in string:
        if i not in new_dict:
            new_dict.update({i: string.count(i)})

    return new_dict


print(string_to_dict(dragon_loot))


def add_to_inventory(inventory, loot):
    for k, v in loot.items():
        if k in inventory:
            inventory[k] += v
        else:
            inventory.update({k: v})
    return inventory


add_to_inventory(stuff, string_to_dict(dragon_loot))

display_inventory(stuff)


def print_picnic(item_dict, left_width, right_width):
    print('PICNIC ITEMS'.center(left_width + right_width, '*'))
    for k, v in item_dict.items():
        print(k.ljust(left_width, '.') + str(v).rjust(right_width))

picnic_item = {'apples': 5, 'cookies': 800, 'potatos': 8, 'dog': 1}

print_picnic(picnic_item, 12, 8)

table_Data = [['apples', 'oranges', 'cherries', 'bananas'], ['Alice', 'Bob', 'Carrol', 'David'],
              ['dogs', 'cats', 'mouses', 'gooses']]


def print_table(table_data):
    col_widths = [0] * len(table_Data)
    for i in range(len(col_widths)):
        col_widths[i] = 1
        for j in table_Data[i]:
            if len(j) > col_widths[i]:
                col_widths[i] = len(j)
        col_widths[i] += 3

    for i in range(len(col_widths)):
        print(table_Data[0][i].ljust(col_widths[0], ' ') + table_Data[1][i].ljust(col_widths[1], ' ') + table_Data[2][
            i].ljust(col_widths[2], ' '))


print_table(table_Data)



