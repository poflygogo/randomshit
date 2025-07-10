# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b674. Is It A Tree
# SEARCC-ISSC 國際學生程式設計競賽

# 並查集 DSU
# 最小生成樹

def is_tree(data: list):
    graph = {}
    for i in range(0, len(data), 2):
        graph[data[i]] = data[i]
        graph[data[i + 1]] = data[i + 1]
    
    # 若總邊數不等於總節點數-1，直接返回False
    if len(data) // 2 != len(graph) - 1:
        return False
    
    for i in range(0, len(data), 2):
        if not union(graph, data[i], data[i + 1]):
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


n = int(input())
while n:
    data = list(map(int, input().split()))
    print('y' if is_tree(data) else 'n')
    n = int(input())
