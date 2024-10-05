def max_prime_factor(n: int) -> int:
    factors = []
    for i in (2, 3):
        if n % i == 0:
            factors.append(i)
    for i in range(5, n // 2 + 1, 6):
        if n % i == 0:
            factors.append(i)
        if n % (i + 2) == 0:
            factors.append(i + 2)
    return max(factors) if factors else n


data = [int(input()) for _ in range(int(input()))]
print(max(data, key=max_prime_factor))
