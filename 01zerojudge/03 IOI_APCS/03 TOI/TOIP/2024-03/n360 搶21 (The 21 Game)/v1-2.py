# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge n360. 搶21 (The 21 Game)
# 2024-03 TOI 練習賽 新手組 第一題


num_target, num_range = map(int, input().split())
print(int(bool(num_target % (num_range + 1))))
