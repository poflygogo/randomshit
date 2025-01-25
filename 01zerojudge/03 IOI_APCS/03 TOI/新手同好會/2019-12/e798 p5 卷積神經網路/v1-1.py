# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e798. p5. 卷積神經網路
# 2019-19 TOI 新手同好會


n = int(input())
data = [tuple(map(int, input().split())) for _ in range(n)]
result = [[0] * (n // 2) for _ in range(n // 2)]

for i in range(n // 2):
    for j in range(n // 2):
        result[i][j] = max(data[x][y] for x in (i * 2, i * 2 + 1) for y in (j * 2, j * 2 + 1))

print('\n'.join(' '.join(map(str, row)) for row in result))
