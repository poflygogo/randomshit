while True:
    try:
        _ = input()
    except EOFError:
        break

    data = list(map(int, input().split()))
    data.sort(key=lambda num: (num % 10, -num // 10))
    
    print(*data)
