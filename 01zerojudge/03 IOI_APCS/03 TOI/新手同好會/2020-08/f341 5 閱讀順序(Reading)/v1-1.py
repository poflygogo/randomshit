# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f341. 5.閱讀順序(Reading)
# 2020-08 TOI 新手同好會


text = input()
axis = input()
idx = text.index(axis)
print(text[idx + len(axis):][::-1] + axis + text[:idx][::-1])
