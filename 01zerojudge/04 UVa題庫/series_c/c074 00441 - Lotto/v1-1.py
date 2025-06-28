# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00441 - Lotto
# ZeroJudge c074

from itertools import combinations

k, *tokens = map(int, input().split())
is_first_case = True
while k:
    tokens.sort()
    if not is_first_case:
        print()
    for i in combinations(tokens, 6):
        print(*i)
    is_first_case = False
    k, *tokens = map(int, input().split())
