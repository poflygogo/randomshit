# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k467. 分班 (Class)
# 2023-04 TOI 練習賽 新手組


n = int(input())
chinese = tuple(map(int, input().split()))
math = tuple(map(int, input().split()))

result1 = []
result2 = []
for i in range(n):
    if chinese[i] > math[i]:
        result1.append(str(i + 1))
    else:
        result2.append(str(i + 1))

if result1:
    print(*result1)
else:
    print('-1')

if result2:
    print(*result2)
else:
    print('-1')
