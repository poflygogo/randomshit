# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11388 GCD LCM
# ZeroJudge d256

for _ in range(int(input())):
    gcd, lcm = map(int, input().split())
    if not lcm % gcd:
        print(gcd, lcm)
    else:
        print('-1')
