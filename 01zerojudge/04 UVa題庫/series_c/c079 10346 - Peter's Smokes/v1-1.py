from sys import stdin


for line in stdin:
    n, k = map(int, line.strip().split())
    count = n
    while n >= k:
        count += n // k
        n = n // k + n % k
    print(count)
