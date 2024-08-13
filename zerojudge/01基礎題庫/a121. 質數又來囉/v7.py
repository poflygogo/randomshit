# 用線性篩法建立質數表
is_prime = [True] * (10000)
primes = []
for i in range(2, 10000):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, 10000, i):
            is_prime[j] = False

# 建好質數表後直接查
while True:
    try:
        a, b = map(int, input().split())
        
        result = sum(1 for prime in primes if a <= prime <= b)

        if b > 10000:
            result += sum(1 for num in range(10001, b + 1, 6) for prime in primes if prime ** 2 < num and num % prime == 0)
            result += sum(1 for num in range(10003, b + 1, 6) for prime in primes if prime ** 2 < num and num % prime == 0)

        print(result)
    except EOFError:
        break
