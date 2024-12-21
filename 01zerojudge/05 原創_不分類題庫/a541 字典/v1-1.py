# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a541. 字典


data = set()
for _ in range(int(input())):
    data.add(input().rstrip())
for _ in range(int(input())):
    text = input().rstrip()
    if text in data:
        print('yes')
    else:
        print('no')
        data.add(text)
