# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a010 因數分解


n = int(input())

factors = {}
for p in (2, 3):
    while n % p == 0:
        n //= p
        factors[p] = factors.get(p, 0) + 1
for p in range(5, int(n ** 0.5) + 1, 6):
    for q in (p, p + 2):
        while n % q == 0:
            n //= q
            factors[q] = factors.get(q, 0) + 1
if n != 1:
    factors[n] = factors.get(n, 0) + 1

print(' * '.join(
    f'{key}{"" if factors[key] == 1 else f"^{factors[key]}"}' for key in sorted(factors)
))
