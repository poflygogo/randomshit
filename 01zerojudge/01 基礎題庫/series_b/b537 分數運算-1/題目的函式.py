from fractions import Fraction as Frac


def func(n: Frac) -> Frac:
    if n == 1:
        return Frac(1)
    if n.is_integer():
        if n % 2 == 0:
            return 1 + func(n / 2)
        else:
            return 1 / func(n - 1)
    return n


while True:
    print(func(Frac(input())))

