# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k466. 成績分析 (Analysis)
# 2023-04 TOI 練習賽 新手組


n, m = map(int, input().split())
progress = []
regress = []

for i in range(1, n + 1):
    info = tuple(map(int, input().split()))
    a = b = 0
    for j in range(1, m):
        if info[j] > info[j - 1]:
            a += info[j] - info[j - 1]
        elif info[j] < info[j - 1]:
            b += info[j - 1] - info[j]
    progress.append((a, i))
    regress.append((b, i))

print(max(progress, key=lambda x: (x[0], -x[1]))[1], max(regress, key=lambda x: (x[0], -x[1]))[1], sep='\n')
