m, n, k = map(int, input().split())
if n == 1 or k <= m + (m - 1) / (n - 1):
    print('YES')
else:
    print('NO')
