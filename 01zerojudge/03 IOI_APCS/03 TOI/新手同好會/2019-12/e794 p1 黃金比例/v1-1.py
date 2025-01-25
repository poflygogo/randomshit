# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e794. p1.黃金比例
# 2019-12 TOI 新手同好會


n = int(input())
a, b = 0, 1
for _ in range(n):
    a, b = b, a + b
print(f'{a}:{b}')
