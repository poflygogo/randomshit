# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a883. D.好忙好忙
# 102-1 延平資研社第二次練習賽


total_jobs = 3
data = [tuple(map(int, input().split())) for _ in range(total_jobs)]
data.sort()
if any(data[i][1] > data[j][0] for i, j in zip(range(total_jobs - 1), range(1, total_jobs))):
    print('QQ')
else:
    print('Happy')
