# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00102 Ecological Bin Packing
# ZeroJudge c081

# 窮舉所有可能的移動數，取最小值

from itertools import permutations

perm = ["".join(i) for i in permutations("BGC", 3)]
while True:
    try:
        arr = list(map(int, input().split()))
        total = sum(arr)
        arr = [arr[i : i + 3] for i in range(0, 9, 3)]
        cost = [
            total - sum(arr[j][i] for i, j in zip(group, range(3)))
            for group in permutations(range(3), 3)
        ]
        ans = min(range(6), key=lambda x: (cost[x], perm[x]))
        print(perm[ans], cost[ans])
    except EOFError:
        break
