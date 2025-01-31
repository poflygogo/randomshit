# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge i376. 尋寶 (Treasure)
# 2022-05 TOI 練習賽 新手組


def treasure():
    for r in range(n):
        temp = [c for c in range(len(data[r])) if data[r][c] == max(data[r])]
        for c in temp:
            if data[r][c] == min(data[i][c] for i in range(n)):
                return f'{r} {c}'
    return 'NO'


n = int(input())
data = [tuple(map(int, input().split())) for _ in range(n)]
print(treasure())
