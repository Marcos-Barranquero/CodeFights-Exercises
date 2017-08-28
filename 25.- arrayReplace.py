# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

"""
Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.

Example

For inputArray = [1, 2, 1], elemToReplace = 1 and substitutionElem = 3, the output should be
arrayReplace(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].
"""

# Code


def arrayReplace(inputArray, elemToReplace, substitutionElem):
    for i, number in enumerate(inputArray):
        if number == elemToReplace:
            inputArray[i] = substitutionElem

    return inputArray
