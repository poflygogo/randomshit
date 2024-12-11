# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10490 Mr. Azad and his Son!!!!!
# ZeroJudge e653


def is_prime(n: int) -> bool:
    if n in primes:
        return True
    if n == 1 or any(n % i == 0 for i in primes):
        return False
    for i in range(35, int(n ** 0.5) + 1, 6):
        if any(n % j == 0 for j in (i, i + 2)):
            return False
    return True


primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
while True:
    num = int(input())
    if num == 0:
        break

    # 若輸入的值不為質數，則結果必定不可能是完全數
    if num not in primes:
        print('Given number is NOT prime! NO perfect number is available.')
    
    # 若輸入的質數並非梅森質數 Mersenne prime，則結果不可能是完全數
    elif is_prime(2 ** num - 1):
        print(f'Perfect: {(2 ** (num - 1) * (2 ** num - 1))}!')
    
    # 確認輸入的值是梅森質數
    else:
        print('Given number is prime. But, NO perfect number is available.')
