move = {
    0: lambda x, y, n: (x, y + n),
    1: lambda x, y, n: (x + n, y),
    2: lambda x, y, n: (x, y - n),
    3: lambda x, y, n: (x - n, y)
}

x, y = 0, 0
for command in range(int(input())):
    direction, step = map(int, input().split())
    x, y = move[direction](x, y, step)
print(x, y)
