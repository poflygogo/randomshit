# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d290. 完全数

# 梅森質數

def is_prime(n: int) -> bool:
    if n == 1:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0:
            return False
        if n % (i + 2) == 0:
            return False
    return True


def prime_generator():
    yield 2
    yield 3
    i = 5
    while True:
        yield i
        yield i + 2
        i += 6


cnt = 0
for p in prime_generator():
    if is_prime(p) and is_prime(2 ** p - 1):
        cnt += 1
        if cnt == 5:
            print(pow(2, p - 1) * (pow(2, p) - 1))
            break
