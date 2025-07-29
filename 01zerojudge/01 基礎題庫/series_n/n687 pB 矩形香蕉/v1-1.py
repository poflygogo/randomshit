# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge n687. pB. 矩形香蕉

# ---------------------------------------------------

import sys
import io
Q = """0 0 10 10 0 0 5 5"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------


x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

xa = max(x1, x3)
xb = min(x2, x4)
ya = max(y1, y3)
yb = min(y2, y4)

if xa >= xb or ya >= yb:
    print("banana")
else:
    print((xb - xa) * (yb - ya))
