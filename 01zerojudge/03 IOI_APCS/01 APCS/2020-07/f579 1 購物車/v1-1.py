# -*- encoding: utf-8 -*-
# python 3.12
# 2020-07 APCS
# ZeroJudge f579


a, b = map(int, input().split())
cnt = 0
for _ in range(int(input())):
    counter = {a : [], b : []}
    for i in input().split():
        i = int(i)
        if abs(i) in (a, b):
            counter[abs(i)].append(1 if i > 0 else -1)
    if all(sum(counter[i]) > 0 for i in counter):
        cnt += 1

print(cnt)
