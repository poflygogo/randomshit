# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a129. 最小生成樹


def mst_weight(arr: list, data: list) -> int:
    data.sort(key=lambda x: x[2])
    edge_cnt = 0
    weight_cnt = 0
    for i, j, d in data:
        if edge_cnt == len(arr) - 1:
            break
        if union(arr, i, j):
            edge_cnt += 1
            weight_cnt += d
    if edge_cnt == len(arr) - 1:
        return weight_cnt
    else:
        return -1


def find(arr: list, x: int) -> int:
    if arr[x] == x:
        return x
    arr[x] = find(arr, arr[x])
    return arr[x]


def union(arr: list, x: int, y: int) -> bool:
    x_root = find(arr, x)
    y_root = find(arr, y)
    if x_root != y_root:
        arr[y_root] = x_root
        return True
    else:
        return False


while True:
    try:
        n, m = map(int, input().split())
        arr = list(range(n))
        data = [tuple(map(int, input().split())) for _ in range(m)]
        print(mst_weight(arr, data))
    except EOFError:
        break
