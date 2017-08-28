# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
"""

# Code


def addBorder(picture):
    largo = len(picture[0])
    bordes = "*" * largo + 2 * "*"
    output = []
    output.append(bordes)
    for renglon in picture:
        output.append("*" + renglon + "*")

    output.append(bordes)
    return(output)
