# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e974. 座位安排 (Seats)
# 2019-05 TOI 練習賽 新手組


row, col, weeks = map(int, input().split())

delta_row = (weeks - 1) // 2
delta_col = weeks // 2

result = [[0] * col for _ in range(row)]
i = 1
for r in range(row):
    for c in range(col):
        result[(r + delta_row) % row][(c + delta_col) % col] = i
        i += 1

print('\n'.join(' '.join(map(str, r)) for r in result))
