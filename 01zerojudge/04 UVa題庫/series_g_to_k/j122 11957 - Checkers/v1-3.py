# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11957 Checkers
# ZeroJudge j122


from functools import lru_cache


@lru_cache(maxsize=None)
def dfs(r: int, c: int):
    if r == 0:
        return 1

    cnt = 0
    if c >= 1:
        if graph[r - 1][c - 1] != 'B':
            cnt += dfs(r - 1, c - 1)
        elif c >= 2 and r >= 2 and graph[r - 2][c - 2] != 'B':
            cnt += dfs(r - 2, c - 2)
    if c + 1 < n:
        if graph[r - 1][c + 1] != 'B':
            cnt += dfs(r - 1, c + 1)
        elif c + 2 < n and r >= 2 and graph[r - 2][c + 2] != 'B':
            cnt += dfs(r - 2, c + 2)
    return cnt


def find_white_chess():
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'W':
                return i, j


for t in range(1, int(input()) + 1):
    n = int(input())
    graph = [input() for _ in range(n)]
    s_r, s_c = find_white_chess()
    print(f'Case {t}: {dfs(s_r, s_c) % 1000007}')
    dfs.cache_clear()
