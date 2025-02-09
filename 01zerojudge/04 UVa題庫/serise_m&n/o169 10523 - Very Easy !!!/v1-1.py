# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10523 Very Easy !!!
# ZeroJudge o169


from sys import stdin

for line in stdin:
    n, a = map(int, line.rstrip().split())
    print(sum(i * pow(a, i) for i in range(1, n + 1)))
