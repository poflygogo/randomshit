# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e999. 2. 巨額獎金(Bonus)
# 2019-05 TOI 練習賽 潛力組


def main():
    n, e = map(int, input().split())
    graph = {i: [] for i in range(n)}
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
    print(bonus(graph, n - 1))


def bonus(graph, target):
    def dfs(curr_vertex):
        nonlocal total_path
        if curr_vertex == target:
            total_path += 1
            return
        for node in graph[curr_vertex]:
            dfs(node)

    total_path = 0
    dfs(0)
    return total_path


if __name__ == '__main__':
    main()
