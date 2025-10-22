# python 3.8
# g309. pC. 傳遞杯子蛋糕(Cupcake)


def dfs(tree: dict, root: int = 0):
    if root == -1:
        return
    k = 1 + sum(i != -1 for i in tree[root]["child"])
    cake = tree[root]["cake"]
    tree[root]["cake"] = cake // k + cake % k
    for i in tree[root]["child"]:
        if i != -1:
            tree[i]["cake"] = cake // k
    dfs(tree, tree[root]["child"][0])
    dfs(tree, tree[root]["child"][1])


def main():
    n, k = map(int, input().split())
    tree = {}
    for _ in range(n):
        a, lft, rgt = map(int, input().split())
        tree[a] = {"child": (lft, rgt), "cake": 0}
    tree[0]["cake"] = k
    dfs(tree)
    print(" ".join(str(tree[i]["cake"] )for i in range(n)))


main()
