# -*- encoding: utf-8 -*-
# python 3.12 
# ZeroJudge f374. 分組 Grouping
# 2020-10 TOI 練習賽 新手組


a, b = map(int, input().split())
group = [[i, 0] for i in range(1, 10)]
idx = 0
while b > 0:
    for _ in range(a):
        if b > 0:
            b, c = divmod(b, 10)
            group[idx][1] += c
        else:
            break
    idx += 1
print(*max(group, key=lambda x: (x[1], x[0])))
