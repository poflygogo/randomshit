# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00941 Permutations
# ZeroJudge n751


from itertools import permutations


for _ in range(int(input())):
    text = input()
    cnt = int(input())
    perm = permutations(text)
    for _ in range(cnt + 1):
        text = next(perm)
    print(''.join(text))
