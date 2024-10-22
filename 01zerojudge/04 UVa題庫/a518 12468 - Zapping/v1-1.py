while True:
    a, b = map(int, input().split())
    if a == b == -1:
        break

    diff = abs(a - b)
    if diff > 50:
        diff = 100 - diff
    print(diff)
