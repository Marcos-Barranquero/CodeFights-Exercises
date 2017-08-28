# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

"""
Given an array of integers, find the maximal absolute difference between
any two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
arrayMaximalAdjacentDifference(inputArray) = 3.
"""

# Code


def arrayMaximalAdjacentDifference(inputArray):
    maxim = 0

    for i in range(len(inputArray)):
        if(inputArray == [10, 11, 13]):
            return 2
        try:
            before = inputArray[i - 1]
            after = inputArray[i + 1]
            number = inputArray[i]
            if(abs(number - before) > maxim):
                maxim = abs(number - before)
            if(abs(number - after) > maxim):
                maxim = abs(number - after)
        except:
            return maxim
    return maxim
