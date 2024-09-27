from sys import stdin


for line in stdin:
    n, m = map(int, line.strip().split())
    if n == m == 0: break

    length = n * m - 1
    data = [next(stdin).strip() for _ in range(length)]
    data.sort()
    for i in range(0, length, m):
        if i + m - 1 == length or data[i] != data[i + m - 1]:
            print(data[i])
            break
