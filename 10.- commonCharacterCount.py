# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

"""
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".

"""

# Code


def commonCharacterCount(s1, s2):
    cont = 0
    s3 = ""
    for i in range(len(s1)):
        cants1 = 0
        cants2 = 0
        if(s1[i] not in s3):
            cants1 = s1.count(s1[i])
            cants2 = s2.count(s1[i])
            s3 += s1[i]
        cont += min(cants1, cants2)

    return cont
