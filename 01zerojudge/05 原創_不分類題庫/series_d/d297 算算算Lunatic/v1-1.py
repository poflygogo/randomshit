from sys import stdin


for n in stdin:
    n = int(n)
    if n % 2 == 0:
        print((n * (n + 2) * (2 * n + 1)) // 8)
    else:
        print((2 * n ** 2 + 3 * n - 1) * (n + 1) // 8)
