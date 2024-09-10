for _ in range(int(input())):
    a, b, c = input().split()
    if b == 'x':
        print(int(a) * int(c))
    else:
        print(int(a) ** int(c))
