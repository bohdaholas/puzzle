"""
Module that deals with puzzle
Github repository: https://github.com/bohdaholas/puzzle.git
"""

board_example = [
 "**** ****",
 "***1 ****",
 "**  3****",
 "* 4 1****",
 "     9 5 ",
 " 6  83  *",
 "3   1  **",
 "  8  2***",
 "  2  ****"
]


def is_number(value):
    """
    Determine whether a value is a number or not
    >>> is_number(5)
    True
    >>> is_number("1")
    True
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def check_row(board):
    """
    Check row according to rules
    >>> check_row(board_example)
    True
    """
    for row in board:
        values = [x for x in row if is_number(x)]
        if len(values) != len(set(values)):
            return False
    return True


def check_column(board):
    """
    Check columns according to rules
    >>> check_column(board_example)
    False
    """
    columns = []
    for i in range(9):
        column = ''
        for row in board:
            column += row[i]
        columns.append(column)
    for column in columns:
        values = [x for x in column if is_number(x)]
        if len(values) != len(set(values)):
            return False
    return True


def get_color_block(board, starting_coords):
    """
    Get each color block
    """
    block = ''
    y, x = starting_coords
    for y in range(y, y + 5):
        if is_number(board[y][x]):
            block += board[y][x]
    for x in range(x, x + 5):
        if is_number(board[y][x]):
            block += board[y][x]
    return block


def check_color_block(board):
    """
    Check color block according to rules
    >>> check_color_block(board_example)
    True
    """
    blocks = []
    for i in range(5):
        coords = (i, 4 - i)
        blocks.append(get_color_block(board, coords))
    for block in blocks:
        if len(block) != len(set(block)):
            return False
    return True


def validate_board(board):
    """
    Bla-bla-bla
    :param board:
    :return:
    >>> validate_board(board_example)
    False
    """
    if check_row(board) and check_column(board) and check_color_block(board):
        return True
    return False
