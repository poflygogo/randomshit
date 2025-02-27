# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11957 Checkers
# ZeroJudge j122


def dfs(r: int, c: int, memo: dict):
    if r == 0:              # 如果已達終點，便返回 1
        return 1
    if (r, c) in memo:      # 如果已經計算過，返回已知的結果
        return memo[(r, c)]

    cnt = 0
    if c >= 1:
        if graph[r - 1][c - 1] != 'B':
            cnt += dfs(r - 1, c - 1, memo)
        elif c >= 2 and r >= 2 and graph[r - 2][c - 2] != 'B':
            cnt += dfs(r - 2, c - 2, memo)
    if c + 1 < n:
        if graph[r - 1][c + 1] != 'B':
            cnt += dfs(r - 1, c + 1, memo)
        elif c + 2 < n and r >= 2 and graph[r - 2][c + 2] != 'B':
            cnt += dfs(r - 2, c + 2, memo)
    
    memo[(r, c)] = cnt      # 緩存結果
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
    print(f'Case {t}: {dfs(s_r, s_c, dict()) % 1000007}')
