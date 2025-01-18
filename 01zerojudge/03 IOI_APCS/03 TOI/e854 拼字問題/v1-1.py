# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e854. 拼字問題
# TOI 初選


expect = input()
exist = input()
exist_counter = {' ': float('inf')}
for c in exist:
    exist_counter[c] = exist_counter.get(c, 0) + 1

for i in range(len(expect)):
    if expect[i] in exist_counter and exist_counter[expect[i]] != 0:
        exist_counter[expect[i]] -= 1
    else:
        print(expect[:i].rstrip())
        break
else:
    print(expect)
