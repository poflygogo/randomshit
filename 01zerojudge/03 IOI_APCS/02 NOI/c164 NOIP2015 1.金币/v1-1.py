# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c164. NOIP2015 1.金币
# NOIP 2015 普及組 第一題


n = int(input())
result = 0
i = 1
while n >= i:
    n -= i
    result += i * i
    i += 1
if n:
    result += i * n
print(result)
