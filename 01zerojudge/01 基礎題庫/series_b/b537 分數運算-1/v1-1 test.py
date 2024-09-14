from fractions import Fraction as Frac


def get_k(n: Frac) -> Frac:
    if n == 1:
        return n
    if n > 1:
        return get_k(n - 1) * 2
    else:
        return get_k(1 / n) + 1


with open('test.txt', 'r', encoding='utf-8') as test:
    for line in test:
        a, b = map(int, line.split())
        print(get_k(Frac(a, b)))
