# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f673. FJCU_109_Winter_Day2_Lab1 樹高


graph = {}
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    graph[a] = (b, c)


def dfs(node, depth=0):
    for i in graph[node]:
        if i == -1:
            global result
            result = max(result, depth)
        else:
            dfs(i, depth + 1)

result = 0
dfs(0)
print(result)
