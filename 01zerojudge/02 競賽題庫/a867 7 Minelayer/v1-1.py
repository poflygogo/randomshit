# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a867. 7. Minelayer
# HP CodeWars 2010


data = [list(input().rstrip()) for _ in range(15)]


def mark(r, c):
    global data
    if data[r][c] == '*':
        return
    if data[r][c] == '.':
        data[r][c] = 1
    else:
        data[r][c] += 1


for row in range(15):
    for col in range(30):
        if data[row][col] != '*':
            continue

        for i in range(row - bool(row != 0), row + bool(row != 14) + 1):
            for j in range(col - bool(col != 0), col + bool(col != 29) + 1):
                mark(i, j)

for line in data:
    print(*line, sep='')