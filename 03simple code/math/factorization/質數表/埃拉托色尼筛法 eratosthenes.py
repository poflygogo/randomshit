def eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]


if __name__ == '__main__':
    num = 100
    result = eratosthenes(num)
    print(f'{num} 以內的質數為:\n',
          *result
          )
