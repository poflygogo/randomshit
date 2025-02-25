# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11934 Magic Formula
# ZeroJudge j031


while True:
    try:
        a, b, c, d, e = map(int, input().split())
    except ValueError:  # 幹林老師最後一筆多一個 0，難怪過不去
        break
    if a == b == c == d == e == 0:
        break
    print(sum(((a * i ** 2 + b * i + c) % d) == 0 for i in range(e + 1)))
