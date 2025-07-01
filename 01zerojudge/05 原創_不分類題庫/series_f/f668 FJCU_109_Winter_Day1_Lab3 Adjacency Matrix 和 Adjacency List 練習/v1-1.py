# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f668. FJCU_109_Winter_Day1_Lab3 Adjacency Matrix 和 Adjacency List 練習


# Adjacency Matrix
n, m = map(int, input().split())
matrix = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1

for i in range(1, n + 1):
    print(f'{i}: {" ".join(str(j) for j in range(1, n + 1) if matrix[i][j] == 1)}')
