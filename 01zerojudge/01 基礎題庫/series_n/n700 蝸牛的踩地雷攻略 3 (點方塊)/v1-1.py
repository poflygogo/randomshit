# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge n700. 蝸牛的踩地雷攻略 3 (點方塊)


direction = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)]

n, m, r, c = map(int, input().split())
data = [input() for _ in range(n)]

graph = [["#"] * m for _ in range(n)]
queue = [(r - 1, c - 1)]
while queue:
    curr_r, curr_c = queue.pop()
    cnt = 0
    temp = []
    for dr, dc in direction:
        nr, nc = curr_r + dr, curr_c + dc
        if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == "#":
            if data[nr][nc] == '*':
                cnt += 1
            else:
                temp.append((nr, nc))
    if cnt > 0:
        graph[curr_r][curr_c] = str(cnt)
    else:
        graph[curr_r][curr_c] = '_'
        queue.extend(temp)

print('\n'.join(''.join(i) for i in graph))
