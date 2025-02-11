# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d626. 小畫家真好用


def dfs(row: int, col: int):
    if not 0 <= row < n or not 0 <= col < n or graph[row][col] == '+':
        return
    graph[row][col] = '+'
    dfs(row + 1, col)
    dfs(row - 1, col)
    dfs(row, col + 1)
    dfs(row, col - 1)


n = int(input())
graph = [list(input()) for _ in range(n)]
dfs(*map(int, input().split()))
print('\n'.join(''.join(r) for r in graph))
