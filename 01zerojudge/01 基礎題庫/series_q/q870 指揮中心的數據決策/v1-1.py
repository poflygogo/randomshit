# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q870. 指揮中心的數據決策


# ---------------------------------------------------

import sys
import io
Q = """
3
1 2 3
7 5 6
3 3 5
"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------


size = int(input())
matrix = [list(map(int, input().split())) for _ in range(size)]

# 紀錄每一行、每一列的總和
sum_row = [sum(i) for i in matrix]
sum_col = [sum(matrix[j][i] for j in range(size)) for i in range(size)]

# 計算列佔優的數量
row_better_cnt = sum(bool(sum_row[i] > sum_col[i]) for i in range(size))

if row_better_cnt > size // 2:
    matrix.sort(key=sum)
    print('\n'.join(' '.join(map(str, i)) for i in zip(*matrix)))
else:
    matrix = [[matrix[j][i] for j in range(size)] for i in range(size)]
    matrix.sort(key=sum)
    print('\n'.join(' '.join(map(str, i)) for i in matrix))
