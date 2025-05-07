# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a456. 子集合


from itertools import combinations

time = int(input())
for t in range(time):
    n = int(input())
    print('{0}')
    for i in range(1, n + 1):
        for j in combinations(range(1, n + 1), i):
            print('{' + ','.join(map(str, j)) + '}')
    if t < time - 1:
        print()
