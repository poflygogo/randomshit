# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00941 Permutations
# ZeroJudge n751


factorial = {i: 1 for i in range(1, 21)}
for i in range(2, 21):
    factorial[i] = factorial[i - 1] * i

for _ in range(int(input())):
    text = sorted(list(input()))
    n = int(input())

    result = 0
    for i in range(len(text) - 1, -1, -1):
        pass
