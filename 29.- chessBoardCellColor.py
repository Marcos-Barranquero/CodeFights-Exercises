# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

"""
Given two cells on the standard chess board, determine whether
they have the same color or not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
chessBoardCellColor(cell1, cell2) = true:
https://codefightsuserpics.s3.amazonaws.com/tasks/chessBoardCellColor/img/example1.png?_tm=1494338560912
"""

# Code


def both_even(n1, n2):
    "Returns true if both numbers are even, false otherwise."
    return n1 % 2 == 0 and n2 % 2 == 0


def both_odd(n1, n2):
    "Returns true if both numbers are odds, false otherwise."
    return n1 % 2 != 0 and n2 % 2 != 0


def is_color(n1, n2):
    "Returns true if the cell is colored, false otherwise."
    return both_even(n1, n2) or both_odd(n1, n2)


def turn_letter_to_number(letter):
    """
    Turns the letter received into its position of the alphabet:
    A -> 1
    B -> 2
    ...
    """
    letters = "ABCDEFGH"
    return letters.index(letter) + 1


def chessBoardCellColor(cell1, cell2):
    c1 = list(cell1)
    c2 = list(cell2)
    c1[1] = int(c1[1])
    c2[1] = int(c2[1])
    c1_color = is_color(turn_letter_to_number(c1[0]), c1[1])
    c2_color = is_color(turn_letter_to_number(c2[0]), c2[1])
    return c1_color == c2_color


if __name__ == "__main__":
    print(chessBoardCellColor("H8", "B3"))
    x = is_color(turn_letter_to_number("H"), 8)
    y = is_color(turn_letter_to_number("B"), 3)
    print(x, y)
    print(x == y)
