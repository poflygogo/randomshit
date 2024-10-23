for _ in range(int(input())):
    print(sum(
        (lambda a, _, c: int(a) * int(c))(*input().split()) for _ in range(int(input()))
    ))
