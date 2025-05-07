# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c705. Int32 to IPv4


from sys import stdin


for n in stdin:
    n = int(n.rstrip())
    result = [0] * 4
    i = 0
    while n > 0:
        result[i] = n & 255
        n >>= 8
        i += 1
    print(*reversed(result), sep='.')
