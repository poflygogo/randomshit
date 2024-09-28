from sys import stdin


for _ in stdin:
    data = stdin.readline().rstrip().split()
    print(*data)

    while len(data) > 0:
        data.reverse()
        del data[-1]
        print(*data)
