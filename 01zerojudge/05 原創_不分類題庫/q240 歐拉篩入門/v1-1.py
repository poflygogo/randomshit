# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q240. 歐拉篩入門
# 題目未公開


# 歐拉篩
n = 2 ** 16
is_prime = [True] * (n + 1)
primes = []

is_prime[0] = is_prime[1] = False
for i in range(2, n + 1):
    if is_prime[i]:
        primes.append(i)
    for j in primes:
        if i * j > n:
            break
        is_prime[i * j] = False
        if i % j == 0:
            break

# 處理輸入、輸出
a = b = 0
while True:
    try:
        num = int(input())
    except EOFError:
        break

    if num < 2 or not is_prime[num]:
        b += num
    else:
        a += num

print(a, b)
