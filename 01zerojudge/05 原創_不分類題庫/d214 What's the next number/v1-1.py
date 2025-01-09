# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d214. What's the next number?

# 穩吃 TLE 的超級暴力解...


def triangle():
    result = 40755
    n = 285
    while True:
        n += 1
        result = n * (n + 1) // 2
        yield result


def pentagonal():
    result = 40755
    n = 165
    while True:
        n += 1
        result = n * (3 * n - 1) // 2
        yield result


def hexagonal():
    result = 40755
    n = 143
    while True:
        n += 1
        result = n * (2 * n - 1)
        yield result


def find():
    t = next(triangle())
    p = next(pentagonal())
    h = 40755

    while t != p != h:
        h = next(hexagonal())
        while p < h:
            p = next(pentagonal())
        if p != h:
            continue
        while t < p:
            t = next(triangle())
    return t


if __name__ == '__main__':
    find()
