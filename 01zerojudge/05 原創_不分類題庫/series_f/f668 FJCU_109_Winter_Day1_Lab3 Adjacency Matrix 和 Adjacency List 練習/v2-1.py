# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f668. FJCU_109_Winter_Day1_Lab3 Adjacency Matrix 和 Adjacency List 練習


# Adjacency List
n, m = map(int, input().split())
matrix = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

for i in range(1, n+1):
    matrix[i].sort()
    print(f'{i}: {" ".join(map(str, matrix[i]))}')
