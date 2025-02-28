# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a783. 5. Houston Skyline
# HP CodeWars 2008


# ------------------------------------------------------------
# 懶得一直複製，直接這樣寫

import sys
import io
test_info = """ 4
                3 3 3
                10 5 2
                4 3 7
                10 1 10
            """
sys.stdin = io.StringIO(test_info.rstrip())

# -------------------------------------------------------------

MAX_WIDTH, MAX_HEIGHT = 50, 20
LAST_LINE = ''.join(str(i % 10) for i in range(1, 51))

while True:
    # 初始化
    height_info = [0] * (MAX_WIDTH + 1)
    max_height = 0
    skyline = [[' '] * (MAX_WIDTH) for _ in range(MAX_HEIGHT)]

    try:
        n = int(input())
    except EOFError:
        break

    # 接受建築資料
    for _ in range(n):
        start, width, height = map(int, input().split())
        if height == 0:     # 高度為 0 的建築是沒有陰影的 (這還是建築嗎?)
            continue

        height += 1
        max_height = max(max_height, height)

        for i in range(start, min(MAX_WIDTH, start + width + 1)):
            height_info[i] = max(height_info[i], height)

    # 每個位置的最高點都標記為 '-'
    for i in range(MAX_WIDTH):
        skyline[height_info[i]][i] = '-'

    # 標記轉角和垂直的陰影
    for col in range(MAX_WIDTH):
        if height_info[col] == height_info[col + 1]:
            continue
        if height_info[col] < height_info[col + 1]:
            for row in range(height_info[col] + 1, height_info[col + 1]):
                skyline[row][col] = '|'
        elif height_info[col] > height_info[col + 1]:
            for row in range(height_info[col + 1] + 1, height_info[col]):
                skyline[row][col] = '|'
        skyline[height_info[col]][col] = '+'
        skyline[height_info[col + 1]][col] = '+'

    # 邊際條件處理
    if height_info[0] > 0:
        for row in range(1, height_info[0]):
            skyline[row][0] = '|'
        skyline[0][0] = '+'
        skyline[height_info[0]][0] = '+'

    # 輸出結果
    print('\n'.join(''.join(i).rstrip() for i in skyline[max_height::-1]))
    print(LAST_LINE)
