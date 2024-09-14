import sys
import math


def sum_factors(n: int):
    factors = {}
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2
    while n % 3 == 0:
        factors[3] = factors.get(3, 0) + 1
        n //= 3
    for i in range(5, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
        i += 2
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
    result = sum([i * factors[i] for i in factors])
    if n > 1:
        result += n
    return result


for num in sys.stdin:
    print(sum_factors(int(num)))
