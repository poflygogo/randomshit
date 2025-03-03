# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b128. 序列長度問題（Sequence）


from sys import stdin
from math import perm   # python 3.6 沒有這個

for n in stdin:
    n = int(n.rstrip())
    print(sum(perm(n, i) * i for i in range(1, n + 1)))
