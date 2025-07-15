# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge i791. pA. 沒有人受傷的世界完成了


from collections import Counter

n, k = map(int, input().split())
gifts = Counter(input().split())
print(sum(i // k for i in gifts.values() if i >= k))
