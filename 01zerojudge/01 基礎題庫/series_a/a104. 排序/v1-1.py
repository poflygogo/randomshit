while True:
    try:
        none = input()
        data = map(int, input().split())
        data = list(data)
        data.sort()
        print(*data)
    except EOFError:
        break
