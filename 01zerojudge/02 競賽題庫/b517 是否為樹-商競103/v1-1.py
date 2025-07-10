# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b517. 是否為樹-商競103
# 103學年度商業類程式設計競賽模擬題

# 使用並查集 DSU 判斷是否為樹
def is_tree(edges: list):
    graph = {}
    for i, j in edges:
        graph[i] = i
        graph[j] = j

    # 若所有節點可構成一個樹，則必定要能滿足: 總邊數 = 總結點數 - 1
    if len(edges) != len(graph) - 1:
        return False

    # 只要有一個節點不連通就直接返回 False
    for i, j in edges:
        if not union(graph, i, j):
            return False
    return True


def find(graph: dict, x: int):
    if graph[x] == x:
        return x
    graph[x] = find(graph, graph[x])
    return graph[x]


def union(graph: dict, x: int, y: int):
    x_root = find(graph, x)
    y_root = find(graph, y)
    if x_root != y_root:
        graph[y_root] = x_root
        return True
    else:
        return False


for _ in range(int(input())):
    ipt = list(map(lambda x: tuple(map(int, x.split(","))), input().split()))
    print("T" if is_tree(ipt) else "F")
