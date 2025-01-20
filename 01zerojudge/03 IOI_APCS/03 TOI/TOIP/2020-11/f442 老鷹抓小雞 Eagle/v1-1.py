# -*- encoding: utf-8 -*-
# python 3.12
# Zerojudge f442. 老鷹抓小雞 Eagle
# 2020-11 TOI 練習賽 新手組


input() # len(chick)
chick = list(map(int, input().split()))
eagle = int(input())
input() # len(trend)
trend = map(int, input().split())

for item in trend:
    idx = chick.index(item)
    eagle, chick[idx] = chick[idx], eagle

print(*chick)
