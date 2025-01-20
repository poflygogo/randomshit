# -*- encoding: utf-8 -*-
# python 3.12
# Zerojudge f441. 評分系統 Score
# 2020-11 TOI 練習賽 新手組


score = int(input().split()[1])
ans = input().split()
for _ in range(int(input())):
    print(score * sum(i == j for i, j in zip(input().split(), ans)))
