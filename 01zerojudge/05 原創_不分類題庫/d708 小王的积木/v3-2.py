from sys import stdin


n = int(next(stdin).strip())
data = [next(stdin).strip() for _ in range(n - 1)]
data.sort()
for i in range(0, n, 2):
    if data[i] != data[i + 1]:
        print(data[i])
        break
