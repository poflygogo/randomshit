# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge h034. 宴會 (Banquet)
# 2021-12 TOI 練習賽 新手組


from itertools import zip_longest


n = int(input())
data = [input() for _ in range(n)]
result = [
    j
    for i in zip_longest(*data, fillvalue='0')
    for j in i
    if j.isalpha()
]

print(''.join(result))
