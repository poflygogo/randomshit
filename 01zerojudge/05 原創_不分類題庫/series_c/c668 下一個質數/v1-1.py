# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c668. 下一個質數


import sys, random
scanner = sys.stdin.readline


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


t, num_min, num_max = map(int, scanner().rstrip().split())
for _ in range(t):
    num = int(scanner().rstrip())
    step = num // 6

    while True:
        temp = step * 6 + 1 # 每 6 個數，測試 2 個，且末位是 5 不必測試
        if temp > num and temp % 5 != 0 and is_prime(temp):
            print(temp)
            break
        temp += 4           # step * 6 + 5
        if temp > num and temp % 5 != 0 and is_prime(temp):
            print(temp)
            break
        step += 1
