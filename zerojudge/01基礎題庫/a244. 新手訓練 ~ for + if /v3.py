for i in range(int(input())):
    a, b, c = [int(n) for n in input().split()]
    if a == 1:print(b + c)
    elif a == 2:print(b - c)
    elif a == 3:print(b * c)
    else:print(int(b / c))
