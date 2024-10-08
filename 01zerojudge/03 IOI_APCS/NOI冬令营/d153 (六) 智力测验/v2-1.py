from sys import stdin


for _ in range(int(stdin.readline().rstrip())):
    n = int(stdin.readline().rstrip())
    data = [int(stdin.readline().rstrip()) for _ in range(n)]
    data.sort()
    print(
        data[n // 2] if n & 1 else data[n // 2 - 1]
    )
