import random
from sys import stdin


def is_prime(n: int, k = 5):
    if n == 1:
        return False
    if n in (2, 3, 5, 7, 11, 13, 17, 19):
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False

    """Miller-Rabin"""
    def is_possible_prime():
        x = pow(a, d, n)
        if x in (1, n - 1):
            return True

        for i in range(s - 1):
            x = x ** 2 % n
            if x == n - 1:
                return True

        return False

    s = 0
    d = n - 1

    while d % 2 == 0:
        s += 1
        d = d >> 1

    for _ in range(k):
        a = random.randint(2, n - 1)
        if not is_possible_prime():
            return False

    return True


for line in stdin:
    a, b = map(int, line.rstrip().split())
    print(sum(True for i in range(a, b + 1) if is_prime(i)))
