# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge n361. 數字旅館 (hotel)
# 2024-03 TOI 練習賽 新手組 第二題


from math import sqrt

n = int(input())
data = tuple(map(int, input().split()))
result = [''] * n
for i in range(n):
    if data[i] % 2 == 0 and data[i] % 3 == 0:
        result[i] = '1'
    elif data[i] % 10 % 2 != 0 and data[i] % 3 != 0:
        result[i] = '2'
    elif sqrt(data[i]).is_integer() or (data[i] % 2 == 0 and data[i] % 7 != 0):
        result[i] = '3'
    else:
        result[i] = '0'
print(' '.join(result))
