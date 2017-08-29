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


def is_color(cell):
    "Returns true if the cell is colored, false otherwise."
    return both_even(cell[0], cell[1]) or both_odd(cell[0], cell[1])


def turn_letter_to_number(letter):
    """
    Turns the letter received into its position of the alphabet:
    """
    letters = "ABCDEFGH"
    return letters.index(letter) + 1


def chessBoardCellColor(cell1, cell2):
    """
    Given two cells on the standard chess board, determine whether
    they have the same color or not.
    """
    c1 = [turn_letter_to_number(cell1[0]), int(cell1[1])]
    c2 = [turn_letter_to_number(cell2[0]), int(cell2[1])]
    return is_color(c1) == is_color(c2)

# @ Tests:


if __name__ == "__main__":
    print(chessBoardCellColor("H8", "B3"))
