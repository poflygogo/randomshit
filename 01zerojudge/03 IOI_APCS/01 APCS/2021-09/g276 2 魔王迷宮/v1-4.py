# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge g276. 2. 魔王迷宮
# 2021-09 APCS

# 主要思路: 不生成矩陣，而是僅記錄炸彈與魔王的座標


row, col, k = map(int, input().split())
boss_info = [list(map(int, input().split())) for _ in range(k)]
bomb = set() # 當前有炸彈的座標
temp = set() # 被魔王踩到的炸彈

while boss_info:
    # 魔王在腳下放炸彈後移動
    for i in range(len(boss_info)):
        bomb.add((boss_info[i][0], boss_info[i][1]))
        boss_info[i][0] += boss_info[i][2]
        boss_info[i][1] += boss_info[i][3]
    
    idx = 0
    while idx < len(boss_info):
        # 踩到炸彈
        if (boss_info[idx][0], boss_info[idx][1]) in bomb:
            r, c, _, _ = boss_info.pop(idx)
            temp.add((r, c))
        # 走出範圍
        elif not 0 <= boss_info[idx][0] < row or not 0 <= boss_info[idx][1] < col:
            boss_info.pop(idx)
        else:
            idx += 1

    bomb -= temp
    temp.clear() # 重置 temp

print(len(bomb))
