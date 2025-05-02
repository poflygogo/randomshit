# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c519. 4. 幻方求解
# 2017高雄市資訊學科能力複賽


side_length, target = map(int, input().split())
graph = [[False] * side_length for _ in range(side_length)]

row, col = 0, side_length // 2
num = 1

while num < target:
    graph[row][col] = True
    num += 1

    r = (row - 1) % side_length
    c = (col + 1) % side_length
    if not graph[r][c]:
        row, col = r, c
        continue
    
    while graph[row][col]:
        row = (row + 1) % side_length

print(row + 1, col + 1)

# 暴力解 bad
