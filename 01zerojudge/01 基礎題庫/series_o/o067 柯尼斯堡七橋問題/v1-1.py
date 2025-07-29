# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge o067. 柯尼斯堡七橋問題


from sys import stdin
from collections import Counter

_, _, *foo = stdin.read().split()
bar = Counter(foo)
baz = sum(1 for i in bar.values() if i % 2 != 0)
if baz < 3:
    print("YES")
else:
    print("NO")
