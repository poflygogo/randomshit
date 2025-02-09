# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge m702. 傑出校友票選活動


from sys import stdin, stdout
from collections import Counter
from heapq import nlargest


n, m = map(int, stdin.readline().split())
votes = Counter(stdin.read().split())
stdout.write(" ".join(nlargest(m, votes.keys(), key=lambda x: (votes[x], x)))+"\n")
