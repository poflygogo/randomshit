# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c705. Int32 to IPv4


from sys import stdin


for n in stdin:
    print(
        *[int(n) >> i & 255 for i in range(24, -1, -8)],
        sep='.'
    )
