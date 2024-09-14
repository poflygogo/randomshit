import sys
import math
from collections import defaultdict


def sum_factors(n: int):
    factors = defaultdict(int)
    while n % 2 == 0:
        factors[2] += 1
        n //= 2
    while n % 3 == 0:
        factors[3] += 1
        n //= 3
    for i in range(5, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors[i] += 1
            n //= i
        i += 2
        while n % i == 0:
            factors[i] += 1
            n //= i
    result = sum([i * factors[i] for i in factors])
    if n > 1:
        result += n
    return result


for num in sys.stdin:
    print(sum_factors(int(num)))
