# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge j249. 111北二2b.市區導航路線規畫
# 111北二區桃竹苗資訊學科能力複賽


# ---------------------------------------------------
# 模擬輸入，不要複製這部分

import sys
import io
Q = """3 3
1 1
2 1
1 1
2 0"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------


import collections

# 讀取資料
m, n = map(int, input().split())    # 東西向與南北向的格子數
p, q = map(int, input().split())    # 灰格數與禁止左轉格數
tx, ty = map(int, input().split())  # 目的地座標
barrier = {tuple(map(int, input().split())) for _ in range(p)}
no_left = {tuple(map(int, input().split())) for _ in range(q)}

# 初始化參數
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)
sx, sy = 0, 0

seen = collections.defaultdict(dict)    # dict[tuple, dict[int, int]]   座標: {方位: 步長}
seen[0, 0] = {0: 0, 1: 0, 2: 0, 3: 0}
queue = [(sx + dx[i], sy + dy[i], i, 1)
         for i in range(2) 
         if (sx + dx[i], sy + dy[i]) not in barrier]

# bfs 主循環
while queue:
    x, y, d, step = queue.pop(0)
    step += 1

    if (x, y) in no_left:
        iterator = [d]
    else:
        iterator = range(4)

    for i in iterator:
        nx, ny = x + dx[i], y + dy[i]
        if (0 <= nx < n and 
            0 <= ny < m and
            (nx, ny) not in barrier and
            seen.get((nx, ny), dict()).get(i, float('inf')) > step):
            seen[(nx, ny)][i] = seen.get((nx, ny), {i: step}).get(i, step)
            queue.append((nx, ny, i, step))

print(min(seen[(tx, ty)].values()))
