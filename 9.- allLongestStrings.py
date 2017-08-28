# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

"""
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

"""

# Code


def allLongestStrings(inputArray):
    maxi = 0
    output = []
    for i in range(len(inputArray)):
        if len(inputArray[i]) > maxi:
            maxi = len(inputArray[i])
    for i in range(len(inputArray)):
        if(len(inputArray[i]) == maxi):
            output.append(inputArray[i])
    return output
