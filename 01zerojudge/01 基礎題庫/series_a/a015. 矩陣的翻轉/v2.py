while True:
    try:
        row, col = map(int, input().split())
    except EOFError:
        break
    data = [input().split() for _ in range(row)]
    result = [[data[j][i] for j in range(row)] for i in range(col)]
    for i in range(col):
        print(*result[i])