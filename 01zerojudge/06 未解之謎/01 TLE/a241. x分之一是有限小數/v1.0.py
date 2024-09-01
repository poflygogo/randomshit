for _ in range(int(input())):
    print(
        sum([1 for i in range(2, int(input()) + 1) if i % 2 == 0 or i % 5 == 0])
    )