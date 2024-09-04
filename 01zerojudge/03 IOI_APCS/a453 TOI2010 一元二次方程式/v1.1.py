for _ in range(int(input())):
    a, b, c = map(int, input().split())
    check = b**2 - 4*a*c
    if check < 0:
        print('No')
        continue
    if (check ** (1/2)).is_integer():
        print('Yes')
    else:
        print('No')