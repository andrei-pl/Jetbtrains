game_board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]


def print_game_board():
    print('---------')
    print(f'| {game_board[0][0]} {game_board[0][1]} {game_board[0][2]} |')
    print(f'| {game_board[1][0]} {game_board[1][1]} {game_board[1][2]} |')
    print(f'| {game_board[2][0]} {game_board[2][1]} {game_board[2][2]} |')
    print('---------')


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def set_coordinate(cmd_text, player):
    coordinate = cmd_text.split(maxsplit=1)
    if len(coordinate) == 1:
        return False, "You should enter numbers!"

    x = coordinate[0]
    y = coordinate[1]
    if not (is_int(x) and is_int(y)):
        return False, "You should enter numbers!"

    ind_x = int(x)
    ind_y = int(y)
    if not(1 <= ind_x <= 3 and 1 <= ind_y <=3):
        return False, "Coordinates should be from 1 to 3!"
    if game_board[ind_x - 1][ind_y - 1] != ' ':
        return False, "This cell is occupied! Choose another one!"

    game_board[ind_x - 1][ind_y - 1] = player
    return True, ""


def is_game_finished():
    player_x_win = game_board[0][0] == game_board[1][0] == game_board[2][0] and game_board[0] == 'X' \
                   or game_board[1][0] == game_board[1][1] == game_board[1][2] and game_board[1][0] == 'X' \
                   or game_board[2][0] == game_board[2][1] == game_board[2][2] and game_board[2][0] == 'X'\
                   or game_board[0][0] == game_board[0][1] == game_board[0][2] and game_board[0] == 'X'\
                   or game_board[1][0] == game_board[1][2] == game_board[1][2] and game_board[0] == 'X' \
                   or game_board[2][0] == game_board[2][1] == game_board[2][2] and game_board[2][0] == 'X' \
                   or game_board[0][0] == game_board[1][1] == game_board[2][2] and game_board[0][0] == 'X' \
                   or game_board[0][2] == game_board[1][1] == game_board[2][0] and game_board[0][2] == 'X'
    player_y_win = game_board[0][0] == game_board[1][0] == game_board[2][0] and game_board[0] == 'O' \
                   or game_board[1][0] == game_board[1][1] == game_board[1][2] and game_board[1][0] == 'O' \
                   or game_board[2][0] == game_board[2][1] == game_board[2][2] and game_board[2][0] == 'O'\
                   or game_board[0][0] == game_board[0][1] == game_board[0][2] and game_board[0] == 'O'\
                   or game_board[1][0] == game_board[1][2] == game_board[1][2] and game_board[0] == 'O' \
                   or game_board[2][0] == game_board[2][1] == game_board[2][2] and game_board[2][0] == 'O' \
                   or game_board[0][0] == game_board[1][1] == game_board[2][2] and game_board[0][0] == 'O' \
                   or game_board[0][2] == game_board[1][1] == game_board[2][0] and game_board[0][2] == 'O'
    if player_x_win:
        return True, 'X wins'
    if player_y_win:
        return True, 'O wins'
    arr = [not any(x for x in row if x == ' ') for row in game_board]
    if all(arr):
        return True, 'Draw'
    return False, ''


err = ""
full_cells = 0
player_turn = 'O'
is_finished = False
player_won = ''

while full_cells < 9 and not is_finished:
    print_game_board()

    if player_turn == 'X':
        player_turn = 'O'
    else:
        player_turn = 'X'

    is_ok = False
    while not is_ok:
        text = input("Enter the coordinates:")
        is_ok, err = set_coordinate(text, player_turn)

        if not is_ok:
            print(err)
        else:
            full_cells += 1

    is_finished, player_won = is_game_finished()

print_game_board()
print(player_won)