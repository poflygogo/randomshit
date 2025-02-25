# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11934 Magic Formula
# ZeroJudge j031


a, b, c, d, e = map(int, input().split())
while any((a, b, c, d, e)):
    mods = [i for i in range(d) if ((a * i ** 2 + b * i + c) / d).is_integer()]
    print(len(mods) * (e // d) + sum((i <= e % d) for i in mods))

    # 待測資修正後即可去掉 try 語句
    try:
        a, b, c, d, e = map(int, input().split())
    except ValueError:
        break
