# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge m800. 辦公室 (Office)
# 2023-12 TOI 練習賽 新手組 第一題


max_row, max_col, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(max_row)]
change = [[0] * max_col for _ in range(max_row)]

for _ in range(k):
    change_next = [change[r].copy() for r in range(max_row)]
    for row in range(max_row):
        for col in range(max_col):
            curr = data[row][col] + change[row][col]
            cnt = cnt_more = cnt_less = 0
            for r, c in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                if 0 <= r < max_row and 0 <= c < max_col:
                    cnt += 1
                    temp = data[r][c] + change[r][c]
                    if temp > curr:
                        cnt_more += 1
                    elif temp < curr:
                        cnt_less += 1
            if cnt_more > cnt // 2:
                change_next[row][col] += 1
            elif cnt_less > cnt // 2:
                change_next[row][col] -= 1
    change = change_next
print(sum(sum(r) for r in change))
