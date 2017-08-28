# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

"""
Some people are standing in a row in a park.
There are trees between them which cannot be moved.
Your task is to rearrange the people by their heights in a
non-descending order without moving the trees.

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

"""

# Code


def sortByHeight(a):
    contador = 0
    ordenados = []
    ordenados += a
    ordenados.sort()
    cant = ordenados.count(-1)
    try:
        for i in range(cant):
            ordenados.remove(-1)
    except:
        pass

    for i in range(len(a)):
        if a[i] != -1:
            a[i] = ordenados[contador]
            contador += 1
    return a
