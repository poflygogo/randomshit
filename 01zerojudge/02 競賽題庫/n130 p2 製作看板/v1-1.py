# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge n130. p2. 製作看板
# 110新北市資訊學科能力複賽 


max_row, max_col = map(int, input().split())
text = input()
graph = [list(input()) for _ in range(max_row)]

slot = [(r, c) for r in range(max_row) for c in range(max_col) if graph[r][c] == '.']
gap = (len(slot) - len(text)) // 2

for i, j in enumerate(range(gap, len(slot) - gap)):
    graph[slot[j][0]][slot[j][1]] = text[i]

print('\n'.join(''.join(line) for line in graph))
