# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e809. 1.字母排序 (Letters)
# 2019-11 TOI 練習賽 潛力組


from bisect import bisect_left


rule = input()
token = input()

counter = [0] * len(rule)
for c in token:
    counter[rule.index(c)] += 1
for i in range(1, len(counter)):
    counter[i] += counter[i - 1]

for _ in range(int(input())):
    print(rule[bisect_left(counter, int(input()))])
