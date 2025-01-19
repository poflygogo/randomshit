# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f338. 2. 后羿射日(Archer)
# 2020-08 TOI 新手同好會


archer_x, archer_y, archer_lv, archer_range = map(int, input().split())
total_sun = int(input())

archer_range **= 2
cnt = 0
for _ in range(total_sun):
    sun_x, sun_y, sun_lv = map(int, input().split())
    if archer_lv >= sun_lv and (archer_x - sun_x) ** 2 + (archer_y - sun_y) ** 2 <= archer_range:
        cnt += 1

print(cnt)
