def euler_sieve(n: int):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return primes


if __name__ == '__main__':
    num = 100
    result = euler_sieve(num)
    print(f'{num} 以內的質數如下:',
          '\n'.join(map(str, result)),
          sep='\n')
