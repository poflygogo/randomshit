# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q366. 1. 十字轟炸
# 113學年度新北新莊高中校內資訊學科能力競賽


max_row, max_col, q = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(max_row)]

data_dict = {data[r][c]: (r, c) for r in range(max_row) for c in range(max_col)}

for _ in range(q):
    target = int(input())
    r, c = data_dict[target]
    result = [data[r - 1][c],
              data[r][c - 1],
              data[(r + 1) % max_row][c],
              data[r][(c + 1) % max_col]]
    result.sort()
    print(' '.join(map(str, result)))
