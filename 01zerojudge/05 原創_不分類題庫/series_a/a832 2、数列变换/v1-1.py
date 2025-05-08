# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a832. 2、数列变换
# 备战 NOIP 2013模拟赛系列


n = int(input())
arr = list(range(1, n + 1))

for k in range(2, n + 1):
    for i in range(0, n // k * k, k):
        arr.insert(i + k - 1, arr.pop(i))
    
    if n % k != 0:
        i = n // k * k
        arr.append(arr.pop(i))

print(' '.join(map(str, arr)))
