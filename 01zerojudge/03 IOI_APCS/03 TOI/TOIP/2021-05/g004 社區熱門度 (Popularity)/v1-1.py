# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge g004. 社區熱門度 (Popularity)
# 2021-05 TOI 練習賽 新手組


from copy import deepcopy


row, col = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(row)]
result = deepcopy(data)
for r in range(row):
    for c in range(col):
        if data[r][c] != 0:
            continue
        temp = [
            data[i][j]
            for i, j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1))
            if 0 <= i < row and 0 <= j < col and data[i][j] != 0
        ]
        if not temp:
            continue
        result[r][c] = sum(temp) // len(temp)

print('\n'.join(' '.join(map(str, line)) for line in result))
