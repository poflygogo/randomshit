# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge m702. 傑出校友票選活動


from sys import stdin
from collections import Counter


m = int(input().split()[1])
data = Counter(stdin.read().splitlines())
print(' '.join(i[0] for i in data.most_common(m)))
