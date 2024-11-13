while True:
    try:
        row, col = map(int, input().split())

    except EOFError:
        break

    else:
        data = [input().split() for _ in range(row)]
        for line in zip(*data):
            print(*line)
