for _ in range(int(input())):
    a, b, c = map(int, input().split())
    check = b**2 - 4*a*c
    print('No' if check < 0 else 'Yes')