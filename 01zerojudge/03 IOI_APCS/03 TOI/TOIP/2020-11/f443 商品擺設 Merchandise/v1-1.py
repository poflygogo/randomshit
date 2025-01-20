# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f443. 商品擺設 Merchandise
# 2020-11 TOI 練習賽 新手組


n = int(input())
volume = tuple(map(int, input().split()))
id = list(map(int, input().split()))

lft = None
for i in range(n):
    if lft is None and volume[i] == -1:
        lft = i
    elif lft is not None and volume[i] == -1:
        if i - lft > 1:
            id_max, id_min = max(range(lft + 1, i), key=lambda x: volume[x]), min(range(lft + 1, i), key=lambda x: volume[x])
            id[id_max], id[id_min] = id[id_min], id[id_max]
        lft = i
print(*id)
