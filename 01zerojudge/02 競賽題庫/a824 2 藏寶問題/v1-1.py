# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a824. 2.藏寶問題
# 100學年度桃竹苗區資訊學科能力競賽


a, b, c = map(int, input().split())
r = sum(i for i in range(1, c + 1) if i % a == 0 or i % b == 0) % 26
print(chr(r + 64))
