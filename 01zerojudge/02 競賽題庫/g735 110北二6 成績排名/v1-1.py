# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge g735. 110北二6.成績排名
# 110北二區桃竹苗資訊學科能力複賽


n = int(input())
score = list(map(int, input().split()))
rank = {i:j for i, j in zip(sorted(score), range(n, 0, -1))}
print(' '.join(str(rank[i]) for i in score))
