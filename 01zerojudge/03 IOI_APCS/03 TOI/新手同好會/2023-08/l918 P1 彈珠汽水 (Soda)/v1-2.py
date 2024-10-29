m, n, k = map(int, input().split())
if n == 1:
    print('YES')
    exit()

total = m
while m >= n:
    total += m // n
    m = m % n + m // n
if total >= k:
    print('YES')
else:
    print('NO')
