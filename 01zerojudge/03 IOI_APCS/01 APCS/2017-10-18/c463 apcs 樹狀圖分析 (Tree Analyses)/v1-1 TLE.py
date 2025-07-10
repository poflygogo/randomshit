# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c463. apcs 樹狀圖分析 (Tree Analyses)


n = int(input())

arr = list(range(n + 1))
leaf = set()

# 紀錄樹的結構，並將葉節點標記起來
for i in range(1, n + 1):
    cnt, *children = map(int, input().split())
    if cnt:
        for j in children:
            arr[j] = i
    else:
        leaf.add(i)

# 紀錄各節點的高度
height = [0] * (n + 1)
for node in leaf:
    cnt = -1
    while True:
        cnt += 1
        height[node] = max(height[node], cnt)
        if arr[node] == node:
            break
        node = arr[node]

print(height.index(max(height)))
print(sum(height))
