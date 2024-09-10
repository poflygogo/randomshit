from sys import stdin
from itertools import accumulate


for line in stdin:
    n, m = map(int, line.split())
    matrix = [[0] * (n + 1)]
    for _ in range(n):
        row = list(map(int, next(stdin).split()))
        row = list(accumulate([0] + row))
        row = [i + j for i, j in zip(matrix[-1], row)]
        matrix.append(row)
    for _ in range(m):
        x1, y1, x2, y2 = map(int, next(stdin).split())
        print(matrix[x2][y2] - matrix[x1-1][y2] - matrix[x2][y1-1] + matrix[x1-1][y1-1])
