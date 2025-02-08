# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00543 Goldbach's Conjecture   # zerojudge 題目編號有誤, 這題應該是 UVa 543
# ZeroJudge c050


from bisect import bisect_left as bisect


def eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [3] + [p for q in range(5, n + 1, 6) for p in (q, q + 2) if primes[p]]    # ignore 2


def main():
    primes = eratosthenes(int(1e6))
    while True:
        n = int(input())
        if not n:
            break
        for a in primes:
            b = n - a
            if primes[bisect(primes, b)] == b:  # same as `b in primes` but faster
                break
        else:
            # 如果跑完整個 for 循環依然沒找到可用的組合，代表哥德巴赫猜想有誤。
            print('Goldbach\'s conjecture is wrong.')
            continue
        print(f'{n} = {a} + {b}')


if __name__ == '__main__':
    main()
