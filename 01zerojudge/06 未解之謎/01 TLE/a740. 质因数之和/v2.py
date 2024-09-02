import sys

def generate_prime(n):
    for i in range(1, n + 1):
        yield 6 * i - 1
        yield 6 * i + 1

for num in sys.stdin:
    num = int(num.strip())
    result = 0
    
    while num % 2 == 0:
        num //= 2
        result += 2
    while num % 3 == 0:
        num //= 3
        result += 3

    for prime in generate_prime(int(num ** 1/2) + 1):
        while num % prime == 0:
            result += prime
            num //= prime
    
    print(result)