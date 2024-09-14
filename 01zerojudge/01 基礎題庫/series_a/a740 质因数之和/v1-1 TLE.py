import sys


def sum_factors(n: int):
    result = 0
    while n % 2 == 0:
        result += 2
        n //= 2
    while n % 3 == 0:
        result += 3
        n //= 3
    for i in range(5, n + 1):
        while n % i == 0:
            result += i
            n //= i
        i += 2
        while n % i == 0:
            result += i
            n //= i
    return result


for num in sys.stdin:
    print(sum_factors(int(num)))
