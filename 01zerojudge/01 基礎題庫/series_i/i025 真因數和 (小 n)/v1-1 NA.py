n = int(input())
factors = set()
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        factors.update({i, n // i})
print(sum(factors) + 1)
