# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k900. 青蛙跳井(1)


a, b, c = map(int,input().split())
print((a - b - 1) // (b - c) + 2)