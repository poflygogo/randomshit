# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge g504. 109北二7.消毒殺菌
# 109北二區桃竹苗資訊學科能力複賽

n, y, *data = map(int, input().split())

time_start = data[0]
time_end = time_start + y
for i in range(0, len(data), 2):
    t = time_end - data[i]
    if t < 0:
        data[i + 1] = 0
        continue
    else:
        data[i + 1] = max(data[i + 1] - t, 0)

print(sum(data[i] for i in range(1, len(data), 2)))
