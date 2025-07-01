# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f670. FJCU_109_Winter_Day1_Lab5 連通塊數量


def dfs(s):
    items.remove(s)
    for i in graph[s]:
        if i in items:
            dfs(i)


n, m = map(int, input().split())
graph = {i: set() for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

items = set(graph)
cnt = 0
for i in range(1, n+1):
    if i in items:
        dfs(i)
        cnt += 1

print(cnt)
