while True:
    try:
        _ = input()
    except EOFError:
        break
    data = input().split()
    data.sort(key=lambda x: int(x))
    print(*data)
