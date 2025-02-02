# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge j536. 不穩定的礦石 (Ore)
# 2022-12 TOI 練習賽 新手組


n, a = map(int, input().split())
ores = list(map(int, input().split()))

idx = ores.index(max(ores))
i = 1
while a > 0 and i <= n:
    if idx + i < n:
        ores[idx] += ores[idx + i]
        ores[idx + i] = 0
        a -= 1
    if idx - i >= 0:
        ores[idx] += ores[idx - i]
        ores[idx - i] = 0
        a -= 1
    i += 1

print(ores[idx], sum(ores) - ores[idx])
