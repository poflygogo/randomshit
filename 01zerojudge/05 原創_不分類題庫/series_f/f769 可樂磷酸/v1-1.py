# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f769. 可樂磷酸

from itertools import accumulate

data = input().lstrip("CA")
a = []
b = []
for i in data:
    if i == "F":
        a.append(0)
        b.append(0)
    elif i == "C":
        a[-1] += 1
    elif i == "A":
        b[-1] += 1

ar = list(accumulate(reversed(a)))
br = list(accumulate(reversed(b)))

for i in range(len(ar) - 1, -1, -1):
    print(ar[i], br[i])
