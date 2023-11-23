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
    row_numbers = []
    column_numbers = []
    is_present = 0
    row_counter = 1
    column_counter = 1

    for row in range(0, 25, 3):
        for field in range(3):
            row_numbers.append(int(board[row][field]))
            row_numbers.append(int(board[row + 1][field]))
            row_numbers.append(int(board[row + 2][field]))
        for number in range(10):
            if number in row_numbers:
                is_present += 1
        if is_present == 9:
            print(f"Row {row_counter} match Sudoku rules")
        else:
            print(f"Row {row_counter} not match Sudoku rules")
        row_numbers = []
        is_present = 0
        row_counter += 1

    print("")

    for column in range(3):
        for field in range(3):
            column_numbers.append(int(board[column][field]))
            column_numbers.append(int(board[column + 3][field]))
            column_numbers.append(int(board[column + 6][field]))
            column_numbers.append(int(board[column + 9][field]))
            column_numbers.append(int(board[column + 12][field]))
            column_numbers.append(int(board[column + 15][field]))
            column_numbers.append(int(board[column + 18][field]))
            column_numbers.append(int(board[column + 21][field]))
            column_numbers.append(int(board[column + 24][field]))

            for number in range(10):
                if number in column_numbers:
                    is_present += 1
            if is_present == 9:
                print(f"Column {column_counter} match Sudoku rules")
            else:
                print(f"Column {column_counter} not match Sudoku rules")

            column_numbers = []
            is_present = 0
            column_counter += 1
    return 0


fill_board(board_data)
draw_board(board_data)
check_board(board_data)
