# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10141 Request for Proposal
# ZeroJudge a535


n, p = map(int, input().split())
t = 1
while (n, p) != (0, 0):
    [input() for _ in range(n)]
    data = {}   # {str:(match,cost)}
    for _ in range(p):
        name = input()
        d, r = input().split()
        data[name] = (-int(r), float(d))
        [input() for _ in range(int(r))]
    if t > 1:
        print()
    print(f'RFP #{t}\n{min(data, key=lambda x: data[x])}')
    t += 1
    n, p = map(int, input().split())
