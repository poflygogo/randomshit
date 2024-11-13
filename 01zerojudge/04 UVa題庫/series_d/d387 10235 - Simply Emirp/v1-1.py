# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10235 Simply Emirp
# ZeroJudge d387
# 
# 題目的範圍很大，一般的輪式篩法不夠快，埃篩/歐拉篩需要的記憶體太多，需要用更快的質數判定法

import random


def is_prime(n, k=5):
    if n < 2:
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


while True:
    try:
        num = int(input())
        num_reverse = int(str(num)[::-1])
        
    except EOFError:
        exit()

    else:
        print(
            num,
            'is',
            'not prime.' if not is_prime(num) else
            'emirp.' if num_reverse != num and is_prime(int(str(num)[::-1])) else
            'prime.'
        )
