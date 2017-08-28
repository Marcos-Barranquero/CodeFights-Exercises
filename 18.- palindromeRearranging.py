# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

"""
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.
"""

# Code


def palindromeRearranging(inputString):

    letras = list(set(inputString))
    solitarias = []

    if(len(set(inputString)) == 0 or len(set(inputString)) == 1):
        return True

    for i in range(len(letras)):
        if inputString.count(letras[i]) == 1:
            solitarias.append(letras[i])

    if len(solitarias) > 1:
        return False

    return True
