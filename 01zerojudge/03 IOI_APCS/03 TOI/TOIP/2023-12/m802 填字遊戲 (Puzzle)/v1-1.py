# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge m802. 填字遊戲 (Puzzle)
# 2023-12 TOI 練習賽 新手組 第三題


n, m = int(input()), int(input())
puzzle = [[None] * n for _ in range(n)]
flag = True
for _ in range(m):
    c, text, col, row = input().split()
    if not flag:
        break

    text, col, row =list(text), int(col), int(row)
    if c == 'V' and all(row + i < n and puzzle[row + i][col] in (None, text[i]) for i in range(len(text))):
        for i in range(len(text)):
            puzzle[row + i][col] = text[i]

    elif c == 'H' and all(col + i < n and puzzle[row][col + i] in (None, text[i]) for i in range(len(text))):
        puzzle[row][col:col + len(text)] = text
    
    else:
        flag = False

print('Yes' if flag else 'No')
