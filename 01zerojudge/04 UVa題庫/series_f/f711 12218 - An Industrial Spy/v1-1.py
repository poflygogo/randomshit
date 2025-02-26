# -*- encoding: utf-8 -*-
# python 3.12
# UVa 12218 An Industrial Spy
# ZeroJudge f711


from itertools import permutations
import random


def is_prime(n, k=5):
    if n == 1:
        return False
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


seen = set()
cnt = 0
for _ in range(int(input())):
    digits = input()
    for i in range(1, len(digits) + 1):
        for j in permutations(digits, i):
            if j[0] == '0':
                continue
            num = int(''.join(j))
            if num not in seen:
                seen.add(num)
                cnt += is_prime(num)
    print(cnt)
    cnt = 0
    seen.clear()
