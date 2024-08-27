while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break

    data = [input().strip() for _ in range(n)]
    data = ''.join(data)

    print(
        *[data[key - 1] for key in tuple(map(int, input().split()))],
        sep=''
    )