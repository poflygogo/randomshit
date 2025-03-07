# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a036. 排列組合


from functools import lru_cache

n = [0] * 100
n[0] = n[1] = 1
for i in range(2, 100):
    n[i] = n[i - 1] * i


@lru_cache(None)
def comb(a, b):
    if a == b:
        return 1
    if b == 1:
        return a
    if b < a // 2:
        b = a - b
    if a < 100:
        return n[a] // n[b] // n[a - b]
    return comb(a - 1, b) + comb(a - 1, b - 1)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(comb(a, b))

