# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge n836. 八卦傳遞


n, m = map(int, input().split())
arr = list(range(n + 1))
size = [1] * (n + 1)


def find(x: int):
    if arr[x] == x:
        return x
    arr[x] = find(arr[x])
    return arr[x]


def union(x: int, y: int):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        if size[x_root] < size[y_root]:
            x_root, y_root = y_root, x_root
        arr[y_root] = x_root
        size[x_root] += size[y_root]


for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

seen = set()
result = []
for i in range(1, n + 1):
    root = find(i)
    if root not in seen:
        seen.add(root)
        result.append(i)

print(result)
