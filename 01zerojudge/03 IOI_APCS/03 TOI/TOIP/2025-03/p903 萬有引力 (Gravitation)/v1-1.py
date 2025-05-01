# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge p903. 萬有引力 (Gravitation)
# TOI 練習賽 新手組


G = 6
m1, m2, r = map(int, input().split())
print(G * m1 * m2 // r ** 2)
