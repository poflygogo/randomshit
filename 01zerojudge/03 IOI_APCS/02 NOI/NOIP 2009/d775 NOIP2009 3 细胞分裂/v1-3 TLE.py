# -*- encoding: utf-8 -*-
# python 3.6
# ZeroJudge d775. NOIP2009 3.细胞分裂
# NOIP 2009


from math import ceil


def cell_division(n: int, m1: int, m2: int, cell_info: list) -> int:
    prime = eratosthenes()
    m = total_tube(m1, m2, prime)
    result = float('inf')
    for i in cell_info:
        i_factors = prime_factorization(i, prime)

        # 代表永遠無法成為 m 的倍數
        if any(m_factor not in i_factors for m_factor in m):
            continue
        result = min(result,
                     max([ceil(m[factor] / i_factors[factor])
                          for factor in m if m[factor] > i_factors[factor]] + [0]))

    if result == float('inf'):
        return -1
    return result


def prime_factorization(n: int, prime: list):
    result = {}
    prime = iter(prime + [1])
    while n > 1:
        p = next(prime)
        if p == 1:
            return {n: 1}
        while n % p == 0:
            n //= p
            result[p] = result.get(p, 0) + 1
    return result


def eratosthenes(n=int(44722)):
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]


def total_tube(a, b, prime) -> dict:
    """ 統計試管總數，用質因數分解的形式表達
    """
    a_dict = prime_factorization(a, prime)
    for i in a_dict:
        a_dict[i] *= b
    return a_dict


def main():
    n = int(input())
    m1, m2 = map(int, input().split())
    cell_info = list(map(int, input().split()))
    print(cell_division(n, m1, m2, cell_info))


if __name__ == '__main__':
    main()
