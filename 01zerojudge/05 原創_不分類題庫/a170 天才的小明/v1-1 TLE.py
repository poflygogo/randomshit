for _ in range(int(input())):
    a, b = map(lambda x: int(x, 8), input().split())
    print(hex(a + b)[2:].upper())
