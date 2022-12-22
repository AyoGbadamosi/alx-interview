#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal's triangle
    of n"""
    if n <= 0:
        return [[]]
    else:
        triangle = [[1], [1, 1]]
        for i in range(2, n):
            accumulator = []
            accumulator.append(1)
            m = i - 1
            for j in range(m):
                accumulator.append(triangle[m][j] + triangle[m][j + 1])
            accumulator.append(1)
            triangle.append(accumulator)
        return triangle
