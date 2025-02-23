# -*- encoding: utf-8 -*-
# python 3.12
# UVa 12626 I ❤ Pizza
# ZeroJudge i918


from collections import Counter

for _ in range(int(input())):
    info = Counter(input())
    print(min(info['M'], info['A'] // 3, info['R'] // 2, info['G'], info['I'], info['T']))
