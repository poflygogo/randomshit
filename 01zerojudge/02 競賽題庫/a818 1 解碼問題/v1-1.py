# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a818. 1.解碼問題
# 101學年度桃竹苗區資訊學科能力競賽


n = int(input())
keyword = {i - 1: j for i, j in zip(map(int, input().split()), range(n))}
text = list(input().rstrip())   # 測資有點問題，字串末端有多餘的空白字元，所以這個 rstrip 不能省
k = int(input())

for _ in range(k):
    temp = [''] * n
    for i, j in enumerate(text):
        temp[keyword[i]] = j
    text = temp

print(''.join(text))
