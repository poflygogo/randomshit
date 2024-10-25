n = num = int(input())
factors = {}
for prime in (2, 3):
    while not n % prime:
        factors[prime] = factors.get(prime, 0) + 1
        n //= prime

for prime in range(5, n + 1, 6):
    for p in (prime, prime + 2):
        while not n % p:
            factors[p] = factors.get(p, 0) + 1
            n //= p
    
    if prime == 1:
        break

print(num, '=', end=' ')
print(*(str(i) if factors[i] == 1 else f"{i}^{factors[i]}" for i in factors), sep=' * ')
