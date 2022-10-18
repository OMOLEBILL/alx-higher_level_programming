#!/usr/bin/python3
"""divides a matric by a number
"""


def matrix_divided(matrix, div):
    """divides a matrix by a number
    """
    if len(matrix) == 0 or type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        "of integers/floats")

    for i in matrix:
        if len(i) == 0:
            raise TypeError("matrix must be a matrix (list of lists)" +
                            "of integers/floats")
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError("matrix must be a matrix (list of lists)" +
                                "of integers/floats")

    rows = [len(i) for i in matrix]
    if len(set(rows)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    z = [[round(j/div, 2) for j in i] for i in matrix]
    return z
