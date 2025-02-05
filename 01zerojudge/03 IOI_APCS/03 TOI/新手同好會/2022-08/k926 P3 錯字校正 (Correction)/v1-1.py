# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k926. P3. 錯字校正 (Correction)
# 2022-08 TOI 練習賽 新手組


s1 = input()
s2 = input()

for _ in range(int(input())):
    s1 = s1.replace(*input().split())

print(sum(i != j for i, j in zip(s1, s2)))
