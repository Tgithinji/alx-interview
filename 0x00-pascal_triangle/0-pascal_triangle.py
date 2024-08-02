#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Implement Pascals triangle
    """
    if n <= 0:
        return []
    triangle = [[1]]

    for _ in range(n-1):
        last_row = triangle[-1]
        next_row = [1]
        for i in range(1, len(last_row)):
            index = last_row[i] + last_row[i-1]
            next_row.append(index)
        next_row.append(1)
        triangle.append(next_row)
    return triangle
