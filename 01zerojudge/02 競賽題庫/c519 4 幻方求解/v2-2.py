# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c519. 4. 幻方求解
# 2017高雄市資訊學科能力複賽


side, target = map(int, input().split())

target_set = (target - 1) // side
offset = target - target_set * side - 1

row = (target_set * 2 - offset) % side
col = (side // 2 - target_set + offset) % side

print(row + 1, col + 1)
