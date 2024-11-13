from sys import stdin


for n in stdin:
    n = int(n) + 1
    count = n - 1
    while n >= 3:
        count += n // 3
        n = n // 3 + n % 3
    print(count)
