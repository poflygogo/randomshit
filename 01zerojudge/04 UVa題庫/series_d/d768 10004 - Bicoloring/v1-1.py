# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10004 Bicoloring
# ZeroJudge d768


from collections import defaultdict


def is_bicolorable(graph):
    # bfs
    color = defaultdict(bool)                       # 使用 bool 代表顏色, 同時兼具紀錄走訪過的節點的功能
    root = max(graph, key=lambda x: len(graph[x]))  # 將鄰接數最多的節點作為根結點
    color[root] = True
    queue = [root]
    while queue:
        vertex = queue.pop(0)
        for w in graph[vertex]:
            if w not in color:
                queue.append(w)
                color[w] = color[vertex] ^ True
            elif color[vertex] == color[w]:
                return False
    return True


def main():
    test_case = int(input())    # 節點總數, 僅用於判斷是否持續循環
    while test_case:
        graph = defaultdict(list)
        for _ in range(int(input())):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)
        if is_bicolorable(graph):
            print('BICOLORABLE.')
        else:
            print('NOT BICOLORABLE.')
        test_case = int(input())


if __name__ == '__main__':
    main()
