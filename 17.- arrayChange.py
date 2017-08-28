# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

"""
You are given an array of integers.
On each move you are allowed to increase exactly one of its element by one.
Find the minimal number of moves required to obtain a
strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3.
"""

# Code


def arrayChange(inputArray):
    contador = 0
    for i in range(len(inputArray)):
        try:
            while inputArray[i] >= inputArray[i + 1]:
                diff = inputArray[i] - inputArray[i + 1] + 1
                inputArray[i + 1] += diff
                contador += diff
        except:
            pass

    return contador


inputArray = [1, 1, 1]
print(arrayChange(inputArray))
