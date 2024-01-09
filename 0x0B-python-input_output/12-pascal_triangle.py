#!/usr/bin/python3
"""Defines the function of a Pascal's Triangle."""


def pascal_triangle(n):
    """Represent the Pascal's Triangle of n.

    Returns:
            list of lists of integers representing the Pascal's triangle of n.
            An empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        trian = triangles[-1]
        tmp = [1]
        for i in range(len(trian) - 1):
            tmp.append(trian[i] + trian[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
