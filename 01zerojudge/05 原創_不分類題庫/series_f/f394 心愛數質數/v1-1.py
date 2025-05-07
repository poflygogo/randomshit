# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f394. 心愛數質數


from sys import stdin
import random


def is_prime(n, k=5):
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Miller-Rabin
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s = s >> 1

    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, s, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


for num in stdin:
    print('Yes' if is_prime(int(num.rstrip())) else 'No')
