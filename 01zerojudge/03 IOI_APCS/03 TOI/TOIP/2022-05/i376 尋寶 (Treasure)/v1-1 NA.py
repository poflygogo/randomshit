# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge i376. 尋寶 (Treasure)
# 2022-05 TOI 練習賽 新手組


n = int(input())
data = [tuple(map(int, input().split())) for _ in range(n)]

for r in range(n):
    # TOFIX: 最大值可能不只一個，需要檢查所有的最大值
    c = data[r].index(max(data[r]))
    if data[r][c] == min(data[i][c] for i in range(n)):
        print(r, c)
        break
else:
    print('NO')
