# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e178. Runningman - 翻牌挑戰

# ---------------------------------------------------

import sys
import io
Q = """
3 1
1 2 3
4 3
0 -1 2 3
3 2
-1 -2 -3"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------


while True:
    try:
        n, k = map(int, input().split())
        positive = []
        negative = []
        for i in input().split():
            t = int(i)
            if t >= 0:
                positive.append(t)
            else:
                negative.append(t)
        
        if k <= len(negative):
            negative.sort()
            print(sum(positive) - sum(negative[:k]) + sum(negative[k:]))
        else:
            positive.extend(list(map(abs, negative)))
            positive.sort()
            k -= len(negative)
            if k % 2 != 0:
                positive[0] *= -1
            print(sum(positive))
    except EOFError:
        break
