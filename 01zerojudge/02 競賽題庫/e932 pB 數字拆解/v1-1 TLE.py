# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e932. pB. 數字拆解
# 2014大學學測推甄申請二階


from functools import lru_cache

@lru_cache(maxsize=100)
def calc(n: int, max_val: int) -> int:
    if n == 0:
        return 1
    if n < 0:
        return 0
    if max_val == 0:
        return 0
    return calc(n - max_val, max_val) + calc(n, max_val - 1)


n = int(input())
print(calc(n, n))
