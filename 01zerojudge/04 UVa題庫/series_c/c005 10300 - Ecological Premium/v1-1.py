for _ in range(int(input())):
    print(sum(
        (lambda a, _, c: a * c)(*map(int, input().split())) for _ in range(int(input()))
    ))
