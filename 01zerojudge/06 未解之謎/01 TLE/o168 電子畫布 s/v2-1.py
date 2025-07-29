# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge o168. 電子畫布 s


from collections import deque


def get_near_node(r: int, c: int):
    if r > 0:
        yield r - 1, c
    if r < h - 1:
        yield r + 1, c
    if c > 0:
        yield r, c - 1
    if c < w - 1:
        yield r, c + 1


h, w, n = map(int, input().split())
canvas = [[0] * w for _ in range(h)]

queue = deque()
seen = set()
for _ in range(n):
    r, c, t, x = map(int, input().split())
    queue.append((r, c, 0))
    seen.add((r, c))
    while queue:
        r, c, step = queue.popleft()
        canvas[r][c] += x
        if step == t:
            continue
        step += 1
        for i, j in get_near_node(r, c):
            if (i, j) not in seen:
                queue.append((i, j, step))
                seen.add((i, j))
    seen.clear()


print("\n".join(" ".join(str(i) for i in row) for row in canvas))
