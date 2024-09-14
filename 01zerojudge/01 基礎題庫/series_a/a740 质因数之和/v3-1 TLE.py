import sys


def prime_generator(n):
    primes = {2, 3}
    yield 2
    yield 3
    for i in range(5, n + 1, 6):
        for p in primes:
            if i % p == 0: break
        else:
            yield i
            primes.add(i)
        i += 2
        for p in primes:
            if i % p == 0: break
        else:
            yield i
            primes.add(i)


def sum_factors(n):
    factors = {}
    for fac in prime_generator(n):
        if fac > n: break
        while n % fac == 0:
            factors[fac] = factors.get(fac, 0) + 1
            n //= fac
    return sum([i * factors[i] for i in factors]) + (n if n != 1 else 0)


for num in sys.stdin:
    print(sum_factors(int(num)))
