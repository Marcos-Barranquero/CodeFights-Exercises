# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

"""
You are given an array of integers representing coordinates of obstacles
situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right.
You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example

For inputArray = [5, 3, 6, 7, 9], the output should be
avoidObstacles(inputArray) = 4.

Check out the image below for better understanding:
https://codefightsuserpics.s3.amazonaws.com/tasks/avoidObstacles/img/example.png?_tm=1490625560816

"""

# Code


def buscaStep(lista, step):
    error = False
    contador = 0
    while(not error):
        try:
            if(lista[step * contador] != "X"):
                contador += 1
            else:
                return False
        except:
            error = True

    return True


def avoidObstacles(inputArray):
    lista = []
    for i in range(max(inputArray) + 2):
        lista.append("O")

    for numero in inputArray:
        lista[numero] = "X"

    for i in range(1, 10):
        if(buscaStep(lista, i)):
            return i
