# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

"""
Ticket numbers usually consist of an even number of digits.
A ticket number is considered lucky if the sum of the first half
of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
isLucky(n) = true;
For n = 239017, the output should be
isLucky(n) = false.

"""

# Code


def isLucky(n):

    # Counters:
    cont1 = 0
    cont2 = 0

    # Transformation to string to indent:
    cadena = str(int(n))
    mitad = len(cadena) // 2

    # Counter 1(first half):
    for i in range(mitad):
        cont1 += int(cadena[i])

    # Counter 2(second half):
    for j in range(mitad, len(cadena)):
        cont2 += int(cadena[j])

    return (cont1 == cont2)
