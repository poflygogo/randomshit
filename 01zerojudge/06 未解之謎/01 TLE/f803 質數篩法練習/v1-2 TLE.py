from bisect import bisect_left


def sieve(n: int):
    def do(k):
        for p in primes:
            if p * k > n:
                break
            is_prime[p * k] = False
            if k % p == 0:
                break

    is_prime = [True] * (n + 1)
    primes = [2]
    do(2)
    primes.append(3)
    do(3)
    for i in range(5, n + 1, 6):
        if is_prime[i]:
            primes.append(i)
        do(i)
        if is_prime[i + 2]:
            primes.append(i + 2)
        do(i + 2)

    return primes


def main():
    n, m = map(int, input().split())
    primes = sieve(n)
    for _ in range(m):
        print(bisect_left(primes, int(input())) + 1)


main()
