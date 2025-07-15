# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k573. pD. 關於病毒傳播這件事

# ---------------------------------------------------

import sys
import io
Q = """
4 4 2 1
0 1
0 2
1 2
2 3
0 99999
"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------

from collections import defaultdict

# 讀取資料
n, m, k, q = map(int, input().split())
graph = defaultdict(set)
info = defaultdict(int)

# 把資料放進去 graph
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].add(v)
    graph[v].add(u)

for _ in range(q):
    a, b = map(int, input().split())

    # bfs
    queue = [(a, 0)]
    seen = {a}
    while queue:
        vertex, step = queue.pop(0)
        if step == k:
            continue
        else:
            step += 1
        for next_vertex in graph[vertex]:
            if next_vertex in seen or info[next_vertex] > k:
                continue
            seen.add(next_vertex)
            queue.append((next_vertex, step))
    print(len(seen))
