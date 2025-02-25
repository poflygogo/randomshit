# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11900 Boiled Eggs
# ZeroJudge j033


for t in range(1, int(input()) + 1):
    n, p, q = map(int, input().split())
    eggs = sorted(map(int, input().split()), reverse=True)

    result = 0
    while eggs and result < p:
        q -= eggs.pop()
        if q < 0:
            break
        result += 1
    print(f'Case {t}: {result}')
