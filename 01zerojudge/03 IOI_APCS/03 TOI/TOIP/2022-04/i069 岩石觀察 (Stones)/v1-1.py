# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge i069. 岩石觀察 (Stones)
# 2022-04 TOI 練習賽 新手組


n = int(input())
stone = list(map(int, input().split()))

average = sum(stone) // n
idx_min, idx_max = stone.index(min(stone)), stone.index(max(stone))
stone[idx_min] += stone[idx_max] - average
stone[idx_max] = average

print(*stone)
