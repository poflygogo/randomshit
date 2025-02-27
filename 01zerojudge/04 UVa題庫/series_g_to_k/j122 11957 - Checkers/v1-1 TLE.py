# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11957 Checkers
# ZeroJudge j122


def dfs(r, c):
    global cnt
    if r == 0:
        cnt += 1
        return
    if c >= 1:
        if graph[r - 1][c - 1] != 'B':
            dfs(r - 1, c - 1)
        elif c >= 2 and r >= 2 and graph[r - 2][c - 2] != 'B':
            dfs(r - 2, c - 2)
    if c + 1 < n:
        if graph[r - 1][c + 1] != 'B':
            dfs(r - 1, c + 1)
        elif c + 2 < n and r >= 2 and graph[r - 2][c + 2] != 'B':
            dfs(r - 2, c + 2)
    

def find_white_chess():
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'W':
                return i, j


for t in range(1, int(input()) + 1):
    n = int(input())
    graph = [input() for _ in range(n)]
    cnt = 0
    s_r, s_c = find_white_chess()
    dfs(s_r, s_c)
    print(f'Case {t}: {cnt % 1000007}')
