# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge n362. 質數遊戲 (Primes)


n = int(input())
a = b = 0
if n % 2 == 0:
    a, b = 2, n // 2
elif n % 3 == 0:
    a, b = 3, n // 3
else:
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0:
            a, b = i, n // i
            break
        i += 2
        if n % i == 0:
            a, b = i, n // i
            break

if b != 0:
    if b == 1:
        a = b = 0
    if b not in (2, 3) and (b % 2 == 0 or 
                            b % 3 == 0 or 
                            any(b % j == 0 for i in range(5, int(b ** 0.5) + 1, 6) for j in (i, i + 2))):
        a = b = 0

print(a, b)
