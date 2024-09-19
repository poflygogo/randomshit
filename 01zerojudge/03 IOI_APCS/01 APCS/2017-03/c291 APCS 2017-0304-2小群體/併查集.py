def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
    return parent[x]


def unite(x, y):
    global parent
    x = find(x)
    y = find(y)
    if x == y: return
    if x <= y:
        parent[x] = y
    else:
        parent[y] = x


while True:
    try:
        n = int(input())
    except EOFError:
        break
    parent = [i for i in range(n)]
    ans = 0
    f = list(map(int, input().split()))
    for i in range(n):
        unite(f[i], i)
    for i in range(n):
        find(i)
    for i in range(n):
        ans += parent[i] == i
    print(ans)
