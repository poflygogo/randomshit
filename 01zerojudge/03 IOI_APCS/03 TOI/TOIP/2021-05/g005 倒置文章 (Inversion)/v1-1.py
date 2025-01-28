# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge g005. 倒置文章 (Inversion)
# 2021-05 TOI 練習賽 新手組


import re


text = re.finditer(r'[+-]+|\w+', '+' + input())
result = []
for item in text:
    try:
        result.append(
            next(text).group() if item.group()[-1] == '+' else
            next(text).group()[::-1]
        )
    except StopIteration:
        break

print(''.join(result))

# 輸入的字串結尾可能有多餘的 +- 符號
# 輸入的字串開頭未必都有 +- 符號
