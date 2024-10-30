while True:
    n = int(input())
    if not n:
        exit()
    n %= 9
    print(n if n else 9)
