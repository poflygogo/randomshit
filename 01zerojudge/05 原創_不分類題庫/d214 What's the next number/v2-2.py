# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d214. What's the next number?

# 簡化後的運算式(忽略過程)
# t = 2h - 1
# p = (1 + √(1 + 24h(2h-1))) / 6, 且 1 + 24h(2h-1) 必須要是完全平方數

# 可以知道 hexagonal 的數字一定都會出現在 triangle 中，hexagonal 是 triangle 的子集


import math


def find():
    h = 144
    while not (temp:=math.sqrt(48 * h ** 2 - 24 * h + 1)).is_integer() or not (temp + 1) % 6 == 0:
        h += 1
    return h * (2 * h - 1)


if __name__ == '__main__':
    print(find())
