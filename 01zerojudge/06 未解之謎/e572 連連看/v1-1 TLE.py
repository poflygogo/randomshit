# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e572. 連連看

# ---------------------------------------------------

import sys
import io
Q = """
10
A B A D A F G H I J
H I A A B J D A F G
0
"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------


from collections import defaultdict


def connection(n: int, arr1: list, arr2: list):
    # dps 窮舉所有可能的路徑
    def dfs(curr: int = 0, last: int = -1, cnt: int = 0):
        if curr >= n:
            nonlocal max_link
            max_link = max(max_link, cnt)
            return
        for i in graph[curr]:
            if i > last:
                dfs(curr + 1, i, cnt + 1)
        dfs(curr + 1, last, cnt)

    pair = defaultdict(list)
    for i in range(n):
        pair[arr1[i]].append(i)

    graph = defaultdict(list)
    for i in range(n):
        for j in pair.get(arr2[i], []):
            graph[j].append(i)

    max_link = 0
    dfs()
    return max_link


def main():
    while True:
        try:
            n = int(input())
            arr1 = input().split()
            arr2 = input().split()
            print(connection(n, arr1, arr2))
        except EOFError:
            break


main()
