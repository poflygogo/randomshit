# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11934 Magic Formula
# ZeroJudge j031


a, b, c, d, e = map(int, input().split())
while any((a, b, c, d, e)):
    print(sum(((a * i ** 2 + b * i + c) % d) == 0 for i in range(e + 1)))
    a, b, c, d, e = map(int, input().split())
