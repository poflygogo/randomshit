from math import gcd


while True:
    n = int(input())
    if not n:
        exit()
    print(sum(gcd(i, j) for i in range(1, n + 1) for j in range(1 + i, n + 1)))
