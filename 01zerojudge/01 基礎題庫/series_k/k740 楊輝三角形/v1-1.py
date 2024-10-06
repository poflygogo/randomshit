def factorial(n: int) -> int:
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


def comb(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


for i in range(1, int(input()) + 1):
    print(*[comb(i - 1, j - 1) for j in range(1, i + 1)])
