# -*- encoding: utf-8 -*-
# python 3.6
# ZeroJudge b128. 序列長度問題（Sequence）


from sys import stdin


def perm(a, b):
    return factorial[a] // factorial[a - b]


LIMIT = 1000 + 1
factorial = [1] * (LIMIT)
for i in range(2, LIMIT):
    factorial[i] = factorial[i - 1] * i

for n in stdin:
    n = int(n.rstrip())
    print(sum(perm(n, i) * i for i in range(1, n + 1)))
