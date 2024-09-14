from math import sqrt, ceil


def factorization(n: int) -> list:
    """
    試除法
    """
    factors = set()
    for i in range(ceil(sqrt(n)), 1, -1):
        if n % i == 0:
            factors.update({i, n // i})
    return sorted(factors)


def fermat_factorization(n: int) -> list:
    """
    利用平方差公式
    n = a^2 + b^2
    n = (a + b)(a - b)
    """

