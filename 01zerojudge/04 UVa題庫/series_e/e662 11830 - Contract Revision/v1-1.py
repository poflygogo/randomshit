# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11830 Contract Revision
# ZeroJudge e662


while True:
    d, n = input().split()
    if d == n == '0':
        break
    n = n.replace(d, '')
    print(int(n) if n else 0)
