# -*- encoding: utf-8 -*-
# python 3.12


# 用 dict 標示所有節點的連接關係
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D'],
    'F': ['D']
}

def dfs(graph, start):
    stack = []
    stack.append(start)
    seen = {start}
    while len(stack) > 0:
        vertex = stack.pop()
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
        print(vertex)

dfs(graph, 'A')
