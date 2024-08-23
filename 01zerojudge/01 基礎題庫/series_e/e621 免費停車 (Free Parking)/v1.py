for i in range(int(input())):
    a, b, c = map(int, input().split())

    data = [i for i in range(a + 1, b) if i % c]
    if data:
        print(*data)
    else:
        print('No free parking spaces.')