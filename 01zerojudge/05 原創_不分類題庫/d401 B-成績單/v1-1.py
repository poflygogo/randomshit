# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJungle d401. B-成績單


n = int(input())
data1 = []
data2 = []
for i in range(n):
    name, score = map(int, input().split())
    if name == 1:
        data1.append(score)
    else:
        data2.append(score)
data1.sort(reverse=True)
data2.sort(reverse=True)

k = int(input()) - 1
if data1[k] > data2[k]:
    print("1", data1[k] - data2[k])
else:
    print("2", data2[k] - data1[k])
