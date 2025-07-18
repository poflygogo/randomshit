# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge p910. 午餐 (Lunch)
# TOI練習賽202506新手組第2題


r, c = map(int, input().split())
foo = {}
for i in range(r):
    bar = input().split()
    for j in range(c):
        if bar[j] == "NA":
            continue
        if bar[j] in foo:
            foo[bar[j]].append((i, j))
        else:
            foo[bar[j]] = [(i, j)]

print("\n".join(f"{i[0] + 1} {i[1] + 1}" for i in foo.get(input(), [(-1, -1)])))
