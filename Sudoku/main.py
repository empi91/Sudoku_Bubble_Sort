import random, time

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
        if i%9 == 0:
            print("-------------------------------")
        if i%3 == 2:
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


def fill_board(board):
    for square_no in range(9):
        if square_no < 3:
            for row in range(0, 7, 3):
                for field in range(3):
                    number = random.randint(1, 9)
                    board[square_no + row][field] = f" {number} "
        elif 2 < square_no < 6:
            for row in range(6, 13, 3):
                for field in range(3):
                    number = random.randint(1, 9)
                    board[square_no + row][field] = f" {number} "
        elif square_no > 5:
            for row in range(12, 19, 3):
                for field in range(3):
                    number = random.randint(1, 9)
                    board[square_no + row][field] = f" {number} "
    return 0

fill_board(board_data)
draw_board(board_data)