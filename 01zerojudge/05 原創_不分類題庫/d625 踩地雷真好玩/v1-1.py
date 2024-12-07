# -*- encoding: utf-8 
# python 3.12
# ZeroJudge d625. 踩地雷真好玩


n = int(input())
data = [list(input()) for _ in range(n)]

for row in range(n):
    for col in range(n):
        if data[row][col] != '*':
            continue

        for r in range(row - 1 if row != 0 else row, row + 2 if row != n - 1 else row + 1):
            for c in range(col - 1 if col != 0 else col, col + 2 if col != n - 1 else col + 1):
                if data[r][c] == '-':
                    data[r][c] = 1
                elif type(data[r][c]) is int:
                    data[r][c] += 1

print('\n'.join(''.join(str(i) for i in row) for row in data))
