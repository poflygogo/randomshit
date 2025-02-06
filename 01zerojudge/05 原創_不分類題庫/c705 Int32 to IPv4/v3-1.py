# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c705. Int32 to IPv4


from sys import stdin


for n in stdin:
    print(
        *[i for i in int(n).to_bytes(4, 'big')],
        sep='.'
    )
