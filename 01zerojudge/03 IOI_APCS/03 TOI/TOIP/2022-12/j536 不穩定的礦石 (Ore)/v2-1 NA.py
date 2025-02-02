# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge j536. 不穩定的礦石 (Ore)
# 2022-12 TOI 練習賽 新手組


n, a = map(int, input().split())
ores = tuple(map(int, input().split()))

idx = ores.index(max(ores))
lft, rgt = idx - a // 2, idx + a // 2

if lft < 0:
    lft, rgt = 0, rgt + abs(lft)
elif rgt >= n:
    lft, rgt = lft - (rgt - n + 1), n - 1

print(sum(ores[lft:rgt + 1]), sum(ores[:lft]) + sum(ores[rgt + 1:]))
