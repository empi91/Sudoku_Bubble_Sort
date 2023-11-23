import random

board_data = [
    [" . ", " . ", " . "], [" . ", " . ", " . "], [" . ", " . ", " . "],
    [" . ", " . ", " . "], [" . ", " . ", " . "], [" . ", " . ", " . "],
    [" . ", " . ", " . "], [" . ", " . ", " . "], [" . ", " . ", " . "],
    [" . ", " . ", " . "], [" . ", " . ", " . "], [" . ", " . ", " . "],
    [" . ", " . ", " . "], [" . ", " . ", " . "], [" . ", " . ", " . "],
    [" . ", " . ", " . "], [" . ", " . ", " . "], [" . ", " . ", " . "],
    [" . ", " . ", " . "], [" . ", " . ", " . "], [" . ", " . ", " . "],
    [" . ", " . ", " . "], [" . ", " . ", " . "], [" . ", " . ", " . "],
    [" . ", " . ", " . "], [" . ", " . ", " . "], [" . ", " . ", " . "],
]


def draw_board(board):
    long_row = "|"
    for i in range(27):
        if i % 9 == 0:
            print("-------------------------------")
        if i % 3 == 2:
            for j in range(3):
                if j == 2:
                    long_row = long_row + board[i][j] + "|"
                else:
                    long_row = long_row + board[i][j]
            print(long_row)
            long_row = "|"
        else:
            for j in range(3):
                if j == 2:
                    long_row = long_row + board[i][j] + "|"
                else:
                    long_row = long_row + board[i][j]
    print("-------------------------------")
    return 0


def find_number(no_list, board, square, row, field):
    while True:
        number = random.randint(1, 9)
        if number in no_list:
            continue
        else:
            no_list.append(number)
            board[square + row][field] = f" {number} "
            break
    return 0


def fill_board(board):
    for square_no in range(9):
        square_numbers = []
        if square_no < 3:
            for row in range(0, 7, 3):
                for field in range(3):
                    find_number(square_numbers, board, square_no, row, field)
        elif 2 < square_no < 6:
            for row in range(6, 13, 3):
                for field in range(3):
                    find_number(square_numbers, board, square_no, row, field)
        elif square_no > 5:
            for row in range(12, 19, 3):
                for field in range(3):
                    find_number(square_numbers, board, square_no, row, field)
    return 0


def check_board(board):
    
    return 0


fill_board(board_data)
draw_board(board_data)
check_board(board_data)
