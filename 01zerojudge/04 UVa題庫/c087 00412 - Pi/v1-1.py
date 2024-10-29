from math import gcd, sqrt
from itertools import combinations


while True:
    n = int(input())
    if not n:
        exit()

    data = [int(input()) for _ in range(n)]
    cnt = 0
    for i, j in combinations(data, 2):
        if gcd(i, j) == 1:
            cnt += 1

    if cnt:
        print(f'{sqrt(n * (n - 1) // 2 * 6 / cnt):.6f}')
    else:
        print('No estimate for this data set.')
