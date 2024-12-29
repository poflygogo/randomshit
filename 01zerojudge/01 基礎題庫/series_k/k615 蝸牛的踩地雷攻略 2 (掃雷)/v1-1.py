# -*- encoding: utf-8 -*-
# python 3.12
# Zerojudge k615. 蝸牛的踩地雷攻略 2 (掃雷)


n, m = map(int, input().split())
data = [list(input()) for _ in range(n)]

for row in range(n):
    for col in range(m):
        if not data[row][col].isdigit():
            continue

        flag = empty = 0
        for r in range(row - (row > 0), row + 1 + (row < n - 1)):
            for c in range(col - (col > 0), col + 1 + (col < m - 1)):
                if data[r][c] == 'P':
                    flag += 1
                elif data[r][c] == '#':
                    empty += 1
        if flag == int(data[row][col]) and empty > 0:
            data[row][col] = 'O'

print('\n'.join(''.join(i for i in row) for row in data))
