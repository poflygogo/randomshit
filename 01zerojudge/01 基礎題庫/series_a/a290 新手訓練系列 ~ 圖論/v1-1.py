# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a290. 新手訓練系列 ~ 圖論


from sys import stdin


def bfs(graph: dict, start: int, end: int):
    queue = [start]
    seen = {start}
    vertex = None
    while queue and vertex != end:
        vertex = queue.pop(0)
        for i in graph[vertex]:
            if i not in seen:
                queue.append(i)
                seen.add(i)
    return vertex == end


def main():
    for line in stdin:
        n, m = map(int, line.split())
        graph = {i: list() for i in range(1, n + 1)}
        for _ in range(m):
            a, b = map(int, stdin.readline().rstrip().split())
            graph[a].append(b)
        a, b = map(int, stdin.readline().rstrip().split())
        print('Yes!!!' if bfs(graph, a, b) else 'No!!!')


if __name__ == '__main__':
    main()
