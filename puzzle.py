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
