# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e788. b3.畢業典禮(Ceremony)
# 2019-12 TOI 練習賽


data = [input().split() + [i] for i in range(int(input()))]
data.sort(key=lambda x: (x[0][-1], x[0][0], x[2]))
for i, j, _ in data:
    print(f'{i[-1]}: {j}')
