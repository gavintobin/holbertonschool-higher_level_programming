#!/usr/bin/python3
"""triang"""


def pascal_triangle(n):
    """func"""
    if n <= 0:
        return []
    tr = [[1]]
    for i in range(1, n):
        r = [1]
        for j in range(1, i):
            r.append(tr[i-1][j-1] + tr[i-1][j])
            r.append(1)
            tr.append(r)
    return tr 
