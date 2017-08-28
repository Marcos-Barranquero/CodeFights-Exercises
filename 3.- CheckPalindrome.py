# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

"""
Given the string, check if it is a palindrome.

Example

For inputString = "aabaa", the output should be
checkPalindrome(inputString) = true;
For inputString = "abac", the output should be
checkPalindrome(inputString) = false;
For inputString = "a", the output should be
checkPalindrome(inputString) = true.

"""

# Code


def checkPalindrome(inputString):
    palabrainvertida = ""
    for i in range(len(inputString) - 1, -1, -1):
        palabrainvertida += inputString[i]

    if palabrainvertida == inputString:
        return True
    else:
        return False
