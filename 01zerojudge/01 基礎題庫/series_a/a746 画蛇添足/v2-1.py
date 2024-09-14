import sys


for line in sys.stdin:
    line = line.strip().split()
    if not line: continue
    n, m = map(int, line)
    x, y = map(int, next(sys.stdin).split())
    mark = [(x, y)]
    for _ in range(m - 1):
        x, y = map(int, next(sys.stdin).split())
        if mark[-1][0] == x:
            if mark[-1][1] < y:
                a, b = mark[-1][1], y + 1
            else:
                a, b = y, mark[-1][1] + 1
            for i in range(a, b):
                mark.append((x, i))
        else:
            if mark[-1][0] < x:
                a, b = mark[-1][0], x + 1
            else:
                a, b = x, mark[-1][0] + 1
            for i in range(a, b):
                mark.append((i, y))
    mark = set(mark)

    for row in range(n + 2):
        if row in (0, n + 1):
            print('-' * (n + 2))
            continue
        for col in range(n + 2):
            if col == 0:
                print('|', end='')
            elif col == n + 1:
                print('|')
            elif (row, col) in mark:
                print('*', end='')
            else:
                print(' ', end='')
        print()
