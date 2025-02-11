# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e990. 奇怪的隕石


from sys import stdin
from math import log2

for line in stdin:
    t, n = map(float, line.rstrip().split())
    print('%.3f' % (-t * log2(n)))
