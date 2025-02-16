# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge n912. 吸血鬼 (Vampire)
# 2024-06 TOI 練習賽 新手組 第三題


def active_hunter():
    global hunter
    temp = set()
    for r, c in hunter:
        for i, j in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= i < max_row and 0 <= j < max_col and (i, j) not in hunter:
                temp.add((i, j))
                if (i, j) in vampire:
                    vampire.remove((i, j))
    hunter = hunter.union(temp)


def active_vampire():
    global vampire
    temp = set()
    for r, c in vampire:
        for i, j in ((r + 1, c + 1), (r + 1, c - 1), (r - 1, c + 1), (r - 1, c - 1)):
            if 0 <= i < max_row and 0 <= j < max_col and (i, j) not in hunter:
                temp.add((i, j))
    vampire = vampire.union(temp)


max_row, max_col, day = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(max_row)]

hunter = set()
vampire = set()
for i in range(max_row):
    for j in range(max_col):
        if data[i][j] == 1:
            hunter.add((i, j))
        elif data[i][j] == -1:
            vampire.add((i, j))

for _ in range(day):
    active_vampire()
    active_hunter()

for r in range(max_row):
    result = ['1' if (r, c) in hunter else '-1' if (r, c) in vampire else '0' for c in range(max_col)]
    print(' '.join(result))
