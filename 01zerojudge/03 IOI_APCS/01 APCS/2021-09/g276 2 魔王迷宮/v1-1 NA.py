# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge g276. 2. 魔王迷宮
# 2021-09 APCS

# 主要思路: 不生成矩陣，而是僅記錄炸彈與魔王的座標


row, col, k = map(int, input().split())
boss_info = [list(map(int, input().split())) for _ in range(k)]
bomb = set()

while k > 0:
    temp = set()

    # 魔王先在腳下放炸彈
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
            k -= 1
        # 走出範圍
        elif not 0 <= boss_info[idx][0] < row or not 0 <= boss_info[idx][1] < col:
            boss_info.pop(idx)
            k -= 1
        else:
            idx += 1

    bomb.difference(temp)

print(len(bomb))
