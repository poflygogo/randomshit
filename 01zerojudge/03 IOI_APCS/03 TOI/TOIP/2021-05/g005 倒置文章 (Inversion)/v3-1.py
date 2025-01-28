# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge g005. 倒置文章 (Inversion)
# 2021-05 TOI 練習賽 新手組


import itertools


text = itertools.groupby(input(), str.isalnum)
result = []
for key, item in text:
    if key:
        result.extend(list(item))
    else:
        try:
            result.extend(list(list(next(text))[1]) if list(item)[-1] == '+' else list(list(next(text))[1])[::-1])
        except StopIteration:
            break

print(''.join(result))
