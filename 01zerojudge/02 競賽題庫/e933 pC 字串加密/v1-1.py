# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e933. pC. 字串加密
# 2014大學學測推甄申請二階


from sys import stdin

s = input().rstrip()
data = stdin.read().splitlines()

s_len = len(s)
result = "impossible"
for w in data:
    if s_len != len(w):
        continue
    t = {i:None for i in s}
    for i, j in zip(s, w):
        if (i == j):
            break
        if t[i] is not None and t[i] != j:
            break
        if t[i] is None and j in t.values():
            break
        t[i] = j

    else:
        result = w
        break
print(result)
