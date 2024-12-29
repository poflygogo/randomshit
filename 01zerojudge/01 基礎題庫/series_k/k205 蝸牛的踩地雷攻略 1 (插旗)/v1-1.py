# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge k205. 蝸牛的踩地雷攻略 1 (插旗)


n, m = map(int, input().split())
data = [list(input()) for _ in range(n)]

for row in range(n):
    for col in range(m):
        if not data[row][col].isdigit():
            continue

        target = int(data[row][col])
        empty = [
            (r, c)
            for r in range(row - 1 if row > 0 else row, row + 2 if row < n - 1 else row + 1)
            for c in range(col - 1 if col > 0 else col, col + 2 if col < m - 1 else col + 1)
            if data[r][c] in {'#', 'P'}
        ]
        
        if len(empty) == target:
            for r, c in empty:
                data[r][c] = 'P'

print('\n'.join(''.join(i for i in row) for row in data))
