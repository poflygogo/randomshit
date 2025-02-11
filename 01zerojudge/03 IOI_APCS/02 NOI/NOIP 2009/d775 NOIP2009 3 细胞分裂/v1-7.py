# -*- encoding: utf-8 -*-
# python 3.6
# ZeroJudge d775. NOIP2009 3.细胞分裂
# NOIP 2009


from math import ceil, sqrt, floor


def cell_division(n: int, m1: int, m2: int, cell_info: list) -> int:
    m_factors = total_tube(m1, m2)
    result = float('inf')

    for num in cell_info:
        if any(num % p != 0 for p in m_factors):
            continue

        num_factors = {}
        for p in m_factors:
            while num % p == 0:
                num //= p
                num_factors[p] = num_factors.get(p, 0) + 1
            if num == 1:
                break

        result = min(result,
                     max([ceil(m_factors[factor] / num_factors[factor])
                          for factor in m_factors if m_factors[factor] > num_factors[factor]] + [0]))

    if result == float('inf'):
        return -1
    return result


def total_tube(a, b) -> dict:
    """ 統計試管總數，用質因數分解的形式表達
    """
    a_dict = {}
    for p in (2, 3):
        while a % p == 0:
            a //= p
            a_dict[p] = a_dict.get(p, 0) + 1
    for q in range(5, floor(sqrt(a)) + 1, 6):
        for p in (q, q + 2):
            while a % p == 0:
                a //= p
                a_dict[p] = a_dict.get(p, 0) + 1
    if a != 1:
        a_dict[a] = 1
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
