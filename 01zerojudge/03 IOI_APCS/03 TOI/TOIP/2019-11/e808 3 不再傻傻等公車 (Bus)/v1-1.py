# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e808. 3.不再傻傻等公車 (Bus)
# 2019-11 TOI 練習賽 新手組


n = int(input())
hour, min = map(int, input().split())
time = [int(input()) for _ in range(n)]

arrive = [0] * (n + 1)
arrive[0] = hour * 60 + min
for i in range(1, n + 1):
    arrive[i] = arrive[i - 1] + time[i - 1]

for i in map(int, input().split()):
    if i == 0:
        break
    result = arrive[i]
    print(f'{result // 60 % 24:02d}:{result % 60:02d}')
