from sys import stdin
import random


def is_prime(n, k=5) -> bool:
    if n == 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    """Miller-Rabin"""
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s = s >> 1

    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, s, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


for line in stdin:
    a, b = map(int, line.rstrip().split())
    print(sum(True for i in range(a, b + 1) if is_prime(i)))
