# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a982. 迷宮問題#1


def bfs(graph, target, start=(1, 1)):
    queue = []
    queue.append(start)
    seen = {start}
    parent = {start: None}

    while len(queue) > 0 and target not in parent:
        vertex = queue.pop(0)
        nodes = [
            (vertex[0] + i, vertex[1] + j)
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1))
            if graph[vertex[0] + i][vertex[1] + j] == '.'
        ]
        for i in nodes:
            if i not in seen:
                queue.append(i)
                seen.add(i)
                parent[i] = vertex
    return parent


n = int(input())
graph = [input() for _ in range(n)]
target = (n - 2, n - 2)
parent = bfs(graph, (n - 2, n - 2))

if target not in parent:
    print('No solution!')
else:
    cnt = 0
    while target is not None:
        cnt += 1
        target = parent[target]
    print(cnt)
