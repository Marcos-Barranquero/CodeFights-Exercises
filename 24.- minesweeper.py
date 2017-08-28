# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

"""
In the popular Minesweeper game you have a board with some mines and those
cells that don't contain a mine have a number in it that indicates the total
number of mines in the neighboring cells. Starting off with some arrangement of
mines we want to create a Minesweeper game setup.

Example

For

matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]
the output should be

minesweeper(matrix) = [[1, 2, 1],
                       [2, 1, 1],
                       [1, 1, 1]]       
Check out the image below for better understanding:
https://codefightsuserpics.s3.amazonaws.com/tasks/minesweeper/img/example.png?_tm=1490636350838
"""

# Code


def minesweeper(matrix):
    n_filas = len(matrix)
    n_columnas = len(matrix[len(matrix) - 1])
    outputmatrix = genera_matriz_output(n_filas, n_columnas)
    print(outputmatrix)

    for fila in range(0, n_filas):
        for columna in range(0, n_columnas):
            vecinos = get_neighbours(matrix, fila, columna)
            numero = vecinos.count(True)
            outputmatrix[fila][columna] = numero
    return outputmatrix


def genera_matriz_output(filas, columnas):
    output = [[0 for i in range(columnas)] for i in range(filas)]
    return output


def get_neighbours(matrix, fila, columna):
    neighbours = []
    for f in range(fila - 1, fila + 2):
        for c in range(columna - 1, columna + 2):
            try:
                if(not(c < 0 or f < 0)):
                    neighbours.append(matrix[f][c])
            except:
                pass

    if (matrix[fila][columna] in neighbours):
        neighbours.remove(matrix[fila][columna])
    return neighbours
