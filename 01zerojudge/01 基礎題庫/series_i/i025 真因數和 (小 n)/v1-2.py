n = int(input())
factors = {1, n}
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        factors.update({i, n // i})
print(sum(factors) - n)
