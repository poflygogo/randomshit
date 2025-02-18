# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge p901. 香料 (Spices)
# 2024-12 TOI 練習賽 新手組 第二題


n = int(input())
spices = tuple(map(int, input().split()))
spices_dict = dict(zip(spices, [(-1,)] * n))
max_row, max_col = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(max_row)]
for i in range(max_row):
    for j in range(max_col):
        if data[i][j] in spices_dict:
            spices_dict[data[i][j]] = (i + 1, j + 1)

for i in spices:
    print(*spices_dict[i])
