from sys import stdin


def dfs(pos, n, ans, tmp):
    if pos == n + 1:
        for i in range(n):
            print(ans[i + 1], end='')
        print()

    for i in range(n, 0, -1):
        if tmp[i] == 0:
            ans[pos] = i
            tmp[i] = 1
            dfs(pos + 1, n, ans, tmp)
            tmp[i] = 0


for s in stdin:
    s = s.strip()
    if s:
        dfs(1, int(s), [0] * 10, [0] * 10)

# 遞迴
