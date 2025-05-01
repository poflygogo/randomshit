# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q098. 因數分解 (Factors)
# TOI 練習賽 潛力組


n = int(input())
t = 9
factors = []
while 1 not in (n, t):
    if n % t == 0:
        n //= t
        factors.append(t)
    else:
        t -= 1

if n != 1:
    print(-1)
else:
    factors.sort()
    print(*factors)
