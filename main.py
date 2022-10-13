from gui import menu
from random import randint
from time import sleep

def board_filler(board_length):
    global k
    global playing_board
    global player_coordinate_y
    global player_coordinate_x

    #Checking for and deleting (if it's needed) not allowed movements
    def movement_check(allowed_movement, not_allowed_movement, possible_movements, tile_list):
        finale_allowed_movements = []
        
        for i in range(len(possible_movements)):
            for j in range(len(tile_list)):
                if possible_movements[i] == j:
                    possible_movements[i] = tile_list[j]
                    break
        
        for i in range(len(possible_movements)):
            finale_allowed_movements.append(possible_movements[i])
        
        for i in range(len(possible_movements)):
            for j in range(len(allowed_movement)):
                if allowed_movement[j] not in possible_movements[i]:
                    finale_allowed_movements.remove(possible_movements[i])
                    break

            for j in range(len(not_allowed_movement)):
                if not_allowed_movement[j] in possible_movements[i] and possible_movements[i] in finale_allowed_movements:
                    finale_allowed_movements.remove(possible_movements[i])
                    break
        return finale_allowed_movements

    def tile_spawning_conditions(y, x, must_not_have_tile_spawning_conditions_list):
        if y != 4:
            if 's' in k and 'w' not in must_not_have_tile_spawning_conditions_list[y + 1][x]:
                must_not_have_tile_spawning_conditions_list[y + 1][x].append('w')
        if x != 4:
            if 'd' in k and 'a' not in must_not_have_tile_spawning_conditions_list[y][x + 1]:
                must_not_have_tile_spawning_conditions_list[y][x + 1].append('a')
        return must_not_have_tile_spawning_conditions_list

    def not_tile_spawning_conditions(y, x, must_have_tile_spawning_conditions_list):
        if y != 4:
            if 's' not in k and 'w' not in must_have_tile_spawning_conditions_list[y + 1][x]:
                must_have_tile_spawning_conditions_list[y + 1][x].append('w')
        if x != 4:
            if 'd' not in k and 'a' not in must_have_tile_spawning_conditions_list[y][x + 1]:
                must_have_tile_spawning_conditions_list[y][x + 1].append('a')
        return must_have_tile_spawning_conditions_list

    def based_array_creator(board_length):
        array = []
        for i in range(board_length):
            l = []
            for j in range(board_length):
                l.append([])
            array.append(l)
        return array

    player_coordinate_x = board_length // 2
    player_coordinate_y = board_length - 1

    spawn_coordinate_x = board_length // 2
    spawn_coordinate_y = board_length - 1


    playing_board = []
    tile_list = {0: [], 1: ['w', 'a', 's', 'd'], 2: ['w', 'a', 'd'], 3: ['a', 's', 'd'], 4: ['w', 's', 'd'], 5: ['w', 'a', 's'], 6: ['s', 'd'], 7: ['a', 's'], 8: ['w', 'd'], 9: ['w', 'a'], 10: ['a'], 11: ['d'], 12: ['w'], 13: ['s'], 14: ['a','d'], 15: ['w', 's']}

    player_spawning_allowed_tiles = [2, 8, 9, 10, 11, 12, 14]

    top_left_allowed_tiles = [0, 6, 11, 13]
    top_right_allowed_tiles = [0, 7, 10, 13]
    bottom_left_allowed_tiles = [0, 8, 11, 12]
    bottom_right_allowed_tiles = [0, 9, 10, 12]

    top_allowed_tiles = [0, 3, 6, 7, 14]
    right_allowed_tiles = [0, 5, 7, 9, 15]
    bottom_allowed_tiles = [0, 2, 8, 9, 14]
    left_allowed_tiles = [0, 4, 6, 8, 15]

    mid_allowed_tiles = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 14, 15]

    must_not_have_tile_spawning_conditions_list = based_array_creator(board_length)
    must_have_tile_spawning_conditions_list = based_array_creator(board_length)

    for y in range(5):
        playing_line = []
        for x in range(5):
            spawn_coordinate_x = 2
            spawn_coordinate_y = 4
            match [y, x]:
                case [spawn_coordinate_y, spawn_coordinate_x]:
                    g = movement_check(must_not_have_tile_spawning_conditions_list[y][x], must_have_tile_spawning_conditions_list[y][x], player_spawning_allowed_tiles, tile_list)
                    k = g[randint(0, len(g) - 1)]
                    playing_line.append(k)
                    must_not_have_tile_spawning_conditions_list = tile_spawning_conditions(y, x, must_not_have_tile_spawning_conditions_list)
                    must_have_tile_spawning_conditions_list = not_tile_spawning_conditions(y, x, must_have_tile_spawning_conditions_list)
                    
                case [0, 0]:
                    g = movement_check(must_not_have_tile_spawning_conditions_list[y][x], must_have_tile_spawning_conditions_list[y][x], top_left_allowed_tiles, tile_list)
                    print(g)
                    k = g[randint(0, len(g) - 1)]
                    playing_line.append(k)
                    must_not_have_tile_spawning_conditions_list = tile_spawning_conditions(y, x, must_not_have_tile_spawning_conditions_list)
                    must_have_tile_spawning_conditions_list = not_tile_spawning_conditions(y, x, must_have_tile_spawning_conditions_list)
                    print(must_not_have_tile_spawning_conditions_list)

                case [0, 4]:
                    g = movement_check(must_not_have_tile_spawning_conditions_list[y][x], must_have_tile_spawning_conditions_list[y][x], top_right_allowed_tiles, tile_list)
                    k = g[randint(0, len(g) - 1)]
                    playing_line.append(k)
                    must_not_have_tile_spawning_conditions_list = tile_spawning_conditions(y, x, must_not_have_tile_spawning_conditions_list)
                    must_have_tile_spawning_conditions_list = not_tile_spawning_conditions(y, x, must_have_tile_spawning_conditions_list)
                    
                case [4, 0]:
                    g = movement_check(must_not_have_tile_spawning_conditions_list[y][x], must_have_tile_spawning_conditions_list[y][x], bottom_left_allowed_tiles, tile_list)
                    k = g[randint(0, len(g) - 1)]
                    playing_line.append(k)
                    must_not_have_tile_spawning_conditions_list = tile_spawning_conditions(y, x, must_not_have_tile_spawning_conditions_list)
                    must_have_tile_spawning_conditions_list = not_tile_spawning_conditions(y, x, must_have_tile_spawning_conditions_list)
                    
                case [4, 4]:
                    g = movement_check(must_not_have_tile_spawning_conditions_list[y][x], must_have_tile_spawning_conditions_list[y][x], bottom_right_allowed_tiles, tile_list)
                    k = g[randint(0, len(g) - 1)]
                    playing_line.append(k)
                    must_not_have_tile_spawning_conditions_list = tile_spawning_conditions(y, x, must_not_have_tile_spawning_conditions_list)
                    must_have_tile_spawning_conditions_list = not_tile_spawning_conditions(y, x, must_have_tile_spawning_conditions_list)
                    
                case [0, _]:
                    g = movement_check(must_not_have_tile_spawning_conditions_list[y][x], must_have_tile_spawning_conditions_list[y][x], top_allowed_tiles, tile_list)
                    k = g[randint(0, len(g) - 1)]
                    playing_line.append(k)
                    must_not_have_tile_spawning_conditions_list = tile_spawning_conditions(y, x, must_not_have_tile_spawning_conditions_list)
                    must_have_tile_spawning_conditions_list = not_tile_spawning_conditions(y, x, must_have_tile_spawning_conditions_list)
                    
                case [_, 4]:
                    g = movement_check(must_not_have_tile_spawning_conditions_list[y][x], must_have_tile_spawning_conditions_list[y][x], right_allowed_tiles, tile_list)
                    k = g[randint(0, len(g) - 1)]
                    playing_line.append(k)
                    must_not_have_tile_spawning_conditions_list = tile_spawning_conditions(y, x, must_not_have_tile_spawning_conditions_list)
                    must_have_tile_spawning_conditions_list = not_tile_spawning_conditions(y, x, must_have_tile_spawning_conditions_list)
                    
                case [4, _]:
                    g = movement_check(must_not_have_tile_spawning_conditions_list[y][x], must_have_tile_spawning_conditions_list[y][x], bottom_allowed_tiles, tile_list)
                    k = g[randint(0, len(g) - 1)]
                    playing_line.append(k)
                    must_not_have_tile_spawning_conditions_list = tile_spawning_conditions(y, x, must_not_have_tile_spawning_conditions_list)
                    must_have_tile_spawning_conditions_list = not_tile_spawning_conditions(y, x, must_have_tile_spawning_conditions_list)
                    
                case [_, 0]:
                    g = movement_check(must_not_have_tile_spawning_conditions_list[y][x], must_have_tile_spawning_conditions_list[y][x], left_allowed_tiles, tile_list)
                    k = g[randint(0, len(g) - 1)]
                    playing_line.append(k)
                    must_not_have_tile_spawning_conditions_list = tile_spawning_conditions(y, x, must_not_have_tile_spawning_conditions_list)
                    must_have_tile_spawning_conditions_list = not_tile_spawning_conditions(y, x, must_have_tile_spawning_conditions_list)
                    
                case [_, _]:
                    g = movement_check(must_not_have_tile_spawning_conditions_list[y][x], must_have_tile_spawning_conditions_list[y][x], mid_allowed_tiles, tile_list)
                    k = g[randint(0, len(g) - 1)]
                    playing_line.append(k)
                    must_not_have_tile_spawning_conditions_list = tile_spawning_conditions(y, x, must_not_have_tile_spawning_conditions_list)
                    must_have_tile_spawning_conditions_list = not_tile_spawning_conditions(y, x, must_have_tile_spawning_conditions_list)
        playing_board.append(playing_line)
    return playing_board

board_length = None
visited_tile_list = []


while True:
    board_length = input()
    if board_length.isnumeric() and int(board_length) % 2 == 1:
        board_length = int(board_length)
        break


filled_board = board_filler(board_length)
#Building a playing board
def board_builder(filled_board, player_coordinate_x, player_coordinate_y):
    from tile_list import tiles_list
    for i in range(5):
        for j in range(5):
            if player_coordinate_x == j and player_coordinate_y == i or [j, i] in visited_tile_list:
                tile_top, _, _, _ = tiles_list(filled_board[i][j])
                print(tile_top, end = '')
                if [j, i] not in visited_tile_list:
                    visited_tile_list.append([j, i])
            else:
                tile_top, _, _, _ = tiles_list([])
                print(tile_top, end = '')

        print('')
        for j in range(5):
            if player_coordinate_x == j and player_coordinate_y == i or [j, i] in visited_tile_list:
                _, tile_mid_with_player, tile_mid_without_player, _ = tiles_list(filled_board[i][j])
                print(tile_mid_with_player if i == player_coordinate_y and j == player_coordinate_x else tile_mid_without_player, end = '')
                if [j, i] not in visited_tile_list:
                    visited_tile_list.append([j, i])
            else:
                _, tile_mid_with_player, tile_mid_without_player, _ = tiles_list([])
                print(tile_mid_with_player if i == player_coordinate_y and j == player_coordinate_x else tile_mid_without_player, end = '')
        print('')
        for j in range(5):
            if (player_coordinate_x == j and player_coordinate_y == i) or [j, i] in visited_tile_list:
                _, _, _, tile_bot = tiles_list(filled_board[i][j])
                print(tile_bot, end = '')
                if [j, i] not in visited_tile_list:
                    visited_tile_list.append([j, i])
            else:
                tile_bot, _, _, _ = tiles_list([])
                print(tile_bot, end = '')
        print('')

print('=========' * board_length)
board_builder(filled_board, 2, 4) 
while True:
    print('=========' * board_length)
    move = input()
    if move == 's' and 's' in filled_board[player_coordinate_y][player_coordinate_x]:
        player_coordinate_y += 1
    if move == 'w' and 'w' in filled_board[player_coordinate_y][player_coordinate_x]:
        player_coordinate_y += -1
    if move == 'd' and 'd' in filled_board[player_coordinate_y][player_coordinate_x]:
        player_coordinate_x += 1
    if move == 'a' and 'a' in filled_board[player_coordinate_y][player_coordinate_x]:
        player_coordinate_x += -1
    if move == 'r':
        visited_tile_list = []
        filled_board = board_filler(board_length)
    sleep(0.1)
    board_builder(filled_board, player_coordinate_x, player_coordinate_y)