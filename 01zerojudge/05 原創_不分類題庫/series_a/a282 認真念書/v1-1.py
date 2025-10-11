while True:
    try:
        n = int(input())
        arr = set(map(int, input().split()))
    except EOFError:
        break

    for i in range(1, n + 2):
        if i not in arr:
            print(i)
            break
