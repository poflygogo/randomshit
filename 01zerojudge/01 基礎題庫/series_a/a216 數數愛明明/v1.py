while True:
    try:
        day = int(input())
    except EOFError:
        break
    a = 0
    b = 0
    for i in range(1, day + 1):
        a += i
        b += a
    print(a, b)
