# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge o927. 鐵路 (Rail)
# TOI練習賽202411潛力組第2題


n, m = map(int, input().split())
arr = [[i, 0] for i in range(n)]


# DSU 模板
def find(x: int):
    if arr[x][0] == x:
        return x
    arr[x][0] = find(arr[x][0])
    return arr[x][0]


def union(x: int, y: int):
    x_root = find(x)
    y_root = find(y)
    arr[x_root][1] += 1
    if x_root != y_root:
        arr[x_root][1] += arr[y_root][1]
        arr[y_root][0] = x_root


for _ in range(m):
    union(*map(int, input().split()))

# 整理節點資料，確保一定會指向根節點
for i in range(n):
    find(i)

# 統計各生成樹分別包含幾個節點、與總連接數
counter = {}
for i, j in arr:
    if i not in counter:
        counter[i] = {"nodes": 1, "links": j}
    else:
        counter[i]["nodes"] += 1
        counter[i]["links"] = max(counter[i]["links"], j)

# 計算有鐵路需要/不需要被停用的路網總數
# 每個路網只需要總結點數-1條鐵路，不符合的都需要拆鐵路
to_stop = do_not_stop = 0
for i in counter.values():
    if i["nodes"] - 1 != i["links"]:
        to_stop += 1
    else:
        do_not_stop += 1

print(to_stop, do_not_stop)
