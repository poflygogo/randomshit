for i in range(1, int(input()) + 1):
    a = int(input())
    b = int(input())
    a = a if a % 2 else a + 1
    print(
        f'Case {i}:',
        sum([j for j in range(a, b + 1, 2)])
    )