# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e913. pA. 彈珠計算
# 2019大學學測推甄申請二階


def marble(max_val: int) -> int:
    if max_val < 5:
        return 0
    prime = [2, 3]
    result = 1
    for i in range(7, max_val + 1, 6):
        a, b = i - 2, i
        if is_prime(prime, a):
            prime.append(a)
        if is_prime(prime, b):
            prime.append(b)
        if prime[-2:] == [a, b]:
            result += 1
    return result


def is_prime(prime: list, n: int) -> bool:
    n_sqrt = int(n ** 0.5)
    for p in prime:
        if p > n_sqrt:
            break
        if n % p == 0:
            return False
    return True


print(marble(int(input())))
