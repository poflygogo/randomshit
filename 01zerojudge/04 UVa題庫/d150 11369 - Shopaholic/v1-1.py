# -*- encoding: utf-8 -*-
# UVa 11369 Shopaholic
# ZeroJudge d150

for _ in range(int(input())):
    item_count = int(input())
    item = sorted(map(int, input().split()), reverse=True)
    print(sum(item[i] for i in range(2, item_count, 3)))
