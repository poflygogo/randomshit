while True:
    n = int(input())
    if n < 0:
        exit()
    print(n * (n + 1) // 2 + 1)
