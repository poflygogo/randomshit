# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k732. 2. 特殊位置
# 2023-06 APCS


n, m = map(int, input().split())
matrix = [tuple(map(int, input().split())) for _ in range(n)]

result = []
for row in range(n):
    for col in range(m):
        x = matrix[row][col]
        if sum(
            matrix[i][j]
            for i in range(row - x if row - x >= 0 else 0, row + x + 1 if row + x + 1 <= n else n)
            for j in range(col - x if col - x >= 0 else 0, col + x + 1 if col + x + 1 <= m else m)
            if abs(row - i) + abs(col - j) <= x) % 10 == x:
            result.append((row, col))

result.sort()
print(
    len(result),
    *[' '.join(str(i) for i in ans) for ans in result],
    sep='\n'
)
