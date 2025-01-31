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

def bfs(graph, start):
    queue = []
    queue.append(start)
    seen = {start}
    while len(queue) > 0:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
        print(vertex)


bfs(graph, 'B')
