# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge g005. 倒置文章 (Inversion)
# 2021-05 TOI 練習賽 新手組


text = input()
result = []
flag = False    # 是否要反轉
start = None    # 紀錄字串區間的起點
for i in range(len(text)):
    if text[i] in '+-':
        if start is not None:
            result.append(text[start:i][::-1 if flag else 1])
            start = None
        flag = bool(text[i] == '-')
    elif start is None:
        start = i

if start is not None:
    result.append(text[start:][::-1 if flag else 1])

print(''.join(result))
