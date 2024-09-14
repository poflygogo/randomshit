import sys
import math


def sum_factors(n: int):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n % 3 == 0:
        factors.append(3)
        n //= 3
    for i in range(5, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
        while n % i == 0:
            factors.append(i)
            n //= i
    result = sum(factors) + (n if n > 1 else 0)
    return result


for num in sys.stdin:
    print(sum_factors(int(num)))
