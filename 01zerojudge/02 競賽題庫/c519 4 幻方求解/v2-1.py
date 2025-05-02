# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c519. 4. 幻方求解
# 2017高雄市資訊學科能力複賽


side, target = map(int, input().split())

# 計算目標數字在第幾組
target_set = (target - 1) // side

row = 0
col = side // 2

# 計算該組數字的第一個數字的座標
row = (row + target_set * 2) % side
col = (col - target_set) % side

# 計算偏移量
target_set = target_set * side + 1
offset = target - target_set

# 計算目標數值的座標
row = (row - offset) % side
col = (col + offset) % side

print(row + 1, col + 1)
