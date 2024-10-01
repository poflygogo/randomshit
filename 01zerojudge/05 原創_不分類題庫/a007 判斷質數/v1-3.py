from sys import stdin


def is_prime(n):
    if n in {2, 3, 5, 7, 11, 13, 17, 19}:
        return True
    for p in {2, 3, 5, 7, 11, 13, 17, 19}:
        if n % p == 0:
            return False
    if n <= 22:
        return False

    # Miller-Rabin
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s = s >> 1

    for a in (2, 7):
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


for num in stdin:
    print('質數' if is_prime(int(num)) else '非質數')
