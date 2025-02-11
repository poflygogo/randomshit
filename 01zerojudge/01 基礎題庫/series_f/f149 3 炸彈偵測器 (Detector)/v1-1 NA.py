# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f149. 3. 炸彈偵測器 (Detector)
# 2020-06 TOI 練習賽 新手組


rows, cols = map(int, input().split())
data = [input().split() for _ in range(rows)]

all_bomb = set()
detected = set()

for row in range(rows):
    for col in range(cols):
        if data[row][col] != '5':
            continue

        temp = set()
        flag = True
        for r in range(max(0, row - 1), min(rows, row + 2)):
            for c in range(max(0, col - 1), min(cols, col + 2)):
                if (r, c) == (row, col):
                    continue
                if data[r][c] == '1':
                    temp.add((r, c))
                elif data[r][c] == '5':
                    flag = False

        all_bomb.update(temp)
        if flag:
            detected.update(temp)

print(len(detected), len(all_bomb.difference(detected)))
