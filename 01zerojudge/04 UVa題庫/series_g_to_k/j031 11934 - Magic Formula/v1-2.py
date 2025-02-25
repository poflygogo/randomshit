# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11934 Magic Formula
# ZeroJudge j031


from sys import stdin

for line in stdin:
    line = line.rstrip()
    if not line:
        continue
    if line == '0 0 0 0 0':
        break
    a, b, c, d, e = map(int, line.rstrip().split())
    print(sum(((a * i ** 2 + b * i + c) % d) == 0 for i in range(e + 1)))
