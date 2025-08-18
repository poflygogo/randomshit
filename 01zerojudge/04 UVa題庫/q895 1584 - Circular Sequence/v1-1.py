# -*- encoding: utf-8 -*-
# python 3.12
# UVa 1584 - Circular Sequence
# ZeroJudge q895


def dna(s: str):
    for _ in range(len(s) + 1):
        yield s
        s = s[1:] + s[0]


for _ in range(int(input())):
    t = input().strip()
    print(min(dna(t)))
