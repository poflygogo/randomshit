# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q367. 2. 木桶問題
# 113學年度新北新莊高中校內資訊學科能力競賽


r = int(input().split()[1])
h = min(map(int, input().split()))
print(str(r * r * h) + 'π')
