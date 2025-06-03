# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge g503. 109北二6.一元多項式計算機
# 109北二區桃竹苗資訊學科能力複賽


n, c, m = map(int, input().split())
data = [tuple(map(int, input().split())) for _ in range(n)]

result = sum(i * c ** j for i, j in data)

result_str = str(result)[::-1][:m]
print(result_str[::-1].zfill(m))
