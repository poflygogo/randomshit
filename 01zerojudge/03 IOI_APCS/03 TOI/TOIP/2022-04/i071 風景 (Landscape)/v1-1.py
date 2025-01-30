# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge i071. 風景 (Landscape)
# 2022-04 TOI 練習賽 新手組


n, m = map(int, input().split())
building = tuple(map(int, input().split()))
m -= 1

cnt = 0
# scan right
curr = building[m]
for i in range(m + 1, n):
    if building[i] > curr:
        curr = building[i]
        cnt += 1

# scan left
curr = building[m]
for i in range(m - 1, -1, -1):
    if building[i] > curr:
        curr = building[i]
        cnt += 1

print(cnt)
