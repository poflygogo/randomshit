from sys import stdin


n = int(next(stdin).strip())
data = sorted([next(stdin).strip() for _ in range(n - 1)])
for i in range(0, n, 2):
    if data[i] != data[i + 1]:
        print(data[i])
        break
