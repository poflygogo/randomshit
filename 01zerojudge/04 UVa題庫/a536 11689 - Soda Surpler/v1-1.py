for _ in range(int(input())):
    a, b, c = map(int, input().split())
    s = a + b

    result = 0
    while s >= c:
        result += s // c
        s = s // c + s % c

    print(result)
