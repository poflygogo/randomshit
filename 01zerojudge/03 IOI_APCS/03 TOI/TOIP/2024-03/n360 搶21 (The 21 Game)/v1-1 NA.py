# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge n360. 搶21 (The 21 Game)
# 2024-03 TOI 練習賽 新手組 第一題


num_target, num_range = map(int, input().split())

while num_target > num_range:
    num_target -= num_range + 1

print(num_target)

# NA(score:85%)
# 這個寫法能過 85% 就很離譜，我輸出的甚至不是合理的答案
