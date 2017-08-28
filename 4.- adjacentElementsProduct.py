# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

"""
Given an array of integers, find the pair of adjacent elements that has the largest
product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.

7 and 3 produce the largest product.
"""

# Code


def adjacentElementsProduct(inputArray):
    maxi = -1000000000
    for i in range(len(inputArray) - 1):
        a = inputArray[i]
        b = inputArray[i + 1]
        c = a * b
        if(c > maxi):
            maxi = c
    return maxi
