def check_prime(num:int)->int:
    num_sqrt = int(num ** 0.5) + 1 
    for prime in primes:
        if prime > num_sqrt:
            return 1
        elif num % prime == 0:
            return 0

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
        
        result = 0
        if b <= 10000:
            for prime in primes:
                if a <= prime <= b:
                    result += 1
                elif prime > b:
                    break

        elif a <= 10000:
            a1 = a + (7 - a % 6) % 6
            a2 = a + 5 - a % 6
            result += sum(1 for num in range(a1, 10000, 6) if num in primes)
            result += sum(1 for num in range(a2, 10000, 6) if num in primes)
            result += sum(1 for num in range(10003, b + 1, 6) if check_prime(num))
            result += sum(1 for num in range(10001, b + 1, 6) if check_prime(num)) 

        else:
            a1 = a + (7 - a % 6) % 6
            a2 = a + 5 - a % 6
            result += sum(1 for num in range(a1, b + 1, 6) if check_prime(num))
            result += sum(1 for num in range(a2, b + 1, 6) if check_prime(num))

        print(result)
    except EOFError:
        break
