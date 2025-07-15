# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k573. pD. 關於病毒傳播這件事

# ---------------------------------------------------

import sys
import io
Q = """
9 10 2 3
0 1
0 3
0 5
2 4
3 4
3 6
4 8
5 6
6 7
6 8
1 10
2 20
7 15
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
    queue = [(a, 0)]
    seen = {a}
    cnt = 1
    while queue:
        vertex, step = queue.pop(0)
        info[vertex] = b
        if step == k:
            continue
        else:
            step += 1
        for next_vertex in graph[vertex]:
            if next_vertex not in seen and info[next_vertex] < b:
                queue.append((next_vertex, step))
                seen.add(next_vertex)
                cnt += 1
    print(cnt)
