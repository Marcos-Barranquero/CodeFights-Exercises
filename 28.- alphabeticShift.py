# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

"""
Given a string, replace each its character by the next one in the English alphabet
(z would be replaced by a).

Example

For inputString = "crazy", the output should be
alphabeticShift(inputString) = "dsbaz".
"""

# Code


def alphabeticShift(inputString):
    """
    Gets an inputString and changes each char it contains
    to the inmediatly next in the alphabet. If the char is 'z',
    it changes into an a.
    """

    outputString = ""
    for letter in inputString:
        if letter == 'z':
            outputString = "".join([outputString, 'a'])
        else:
            outputString = "".join([outputString, chr(ord(letter) + 1)])

    return outputString


print(alphabeticShift("zaklsdhkjsahd"))
