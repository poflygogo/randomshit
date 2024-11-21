# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge k402. 費氏數列


from functools import lru_cache
from time import time


@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(int(input())))
