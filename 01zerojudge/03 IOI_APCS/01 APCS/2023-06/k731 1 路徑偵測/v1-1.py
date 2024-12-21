# -*- encoding: utf-8 -*-
# python 3.12
# Zerojudge k731. 1. 路徑偵測
# 2023-06 APCS


# 初始座標(x, y) = (0, 0)
# direction 介於 0-3 之間，代表東、北、西、南
# direction_change 為 list[int] 分別表示方向不變、左轉、迴轉、右轉的次數
x = y = 0
direction = 0
direction_change = [0, 0, 0, 0]
for _ in range(int(input())):
    a, b = map(int, input().split())
    mov_x, mov_y = a - x, b - y
    x, y = a, b

    direction_temp = (mov_y > 0) + (mov_x < 0) * 2 + (mov_y < 0) * 3
    turn = (4 + direction_temp - direction) % 4
    direction_change[turn] += 1
    direction = direction_temp

# 調整要輸出的值與順序
del direction_change[0]
direction_change.append(direction_change.pop(1))

print(*direction_change)
