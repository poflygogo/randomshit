# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c143. 105北二1爺爺種樹


max_col, max_row = map(int, input().split())
tree = set()
for _ in range(int(input())):
    c1, r1, c2, r2 = map(int, input().split())
    if r1 > r2:     # swap
        c1, r1, c2, r2 = c2, r2, c1, r1
    if r1 == r2:
        c1, c2 = sorted([c1, c2])
        tree.update({(r1, c) for c in range(c1, c2 + 1)})
    elif c1 == c2:
        r1, r2 = sorted([r1, r2])
        tree.update({(r, c1) for r in range(r1, r2 + 1)})
    elif r2 > r1 and c2 > c1:       # slope = 1
        tree.update({(r, c) for r, c in zip(range(r1, r2 + 1), range(c1, c2 + 1))})
    else:                           # slope = -1
        tree.update({(r, c) for r, c in zip(range(r1, r2 + 1), range(c1, c2 - 1, -1))})
print(len(tree))
