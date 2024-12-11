# -*- encoding: utf-8 -*-
# python 3.12
# UVa 12820 Cool Word
# ZeroJudge e706


cases = 0
while True:
    try:
        n = int(input())
    except EOFError:
        break
    else:
        cases += 1
        cnt = 0
        for _ in range(n):
            counter = {}
            text = input()
            for i in text:
                counter[i] = counter.get(i, 0) + 1
            if len(counter) >= 2 and len(counter) == len(set(counter.values())):
                cnt += 1
        print(f'Case {cases}: {cnt}')
