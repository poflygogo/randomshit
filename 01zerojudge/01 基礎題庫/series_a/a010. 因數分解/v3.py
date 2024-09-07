num = int(input())

primes = {}
while num % 2 == 0:
    primes[2] = primes.get(2, 0) + 1
    num //= 2

while num % 3 == 0:
    primes[3] = primes.get(3, 0) + 1
    num //= 3

for pri in range(5, num + 1, 6):
    while num % pri == 0:
        primes[pri] = primes.get(pri, 0) + 1
        num //= pri
    while num % (pri + 2) == 0:
        primes[pri + 2] = primes.get(pri + 2, 0) + 1
        num //= pri + 2

result = []
for pri in sorted(list(primes.keys())):
    result.append(
        f'{pri}^{primes[pri]}' if primes[pri] > 1 else pri
    )
print(
    *result,
    sep=' * '
)