# -*- encoding: utf-8 -*-
# python 3.12
# 2020-10 APCS
# ZeroJudge f312


a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
n = int(input())
print(max(a1 * (i ** 2) + b1 * i + c1 + a2 * ((n - i) ** 2) + b2 * (n - i) + c2 for i in range(n + 1)))
