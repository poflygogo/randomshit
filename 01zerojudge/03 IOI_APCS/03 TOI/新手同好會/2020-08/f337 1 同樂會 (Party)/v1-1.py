# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f337. 1.同樂會 (Party)
# 2020-08 TOI 新手同好會


n, m = map(int, input().split())
less = n * 2
more = less + n
m *= 8

if less <= m <= more:
    print('Yes')
elif m < less:
    print('Not enough')
else:
    print('Too much')
