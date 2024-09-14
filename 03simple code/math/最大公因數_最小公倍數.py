def gcd1(a: int, b: int):
    while b:
        a, b = b, a % b
    return a


def gcd2(a: int, b: int):
    return a if b == 0 else gcd2(b, a % b)


def lcm1(a: int, b: int):
    n, m = a, b
    while m:
        n, m = m, n % m
    return a * b // n


def lcm2(a: int, b: int):
    return a * b // gcd2(a, b)
