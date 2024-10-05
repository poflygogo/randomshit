import math


def func(n: int):
    if n > 10:
        return 2 * math.sqrt(n)
    if n > -10:
        return -0.5 * n + 10
    return abs(n ** 5) - 33
    

print(f'{func(int(input())):.1f}')
