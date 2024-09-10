for _ in range(int(input())):
    cacu = input()
    a, b = map(int, input().split(cacu))
    if cacu == '+':
        print(a + b)
    else:
        print(a - b)
