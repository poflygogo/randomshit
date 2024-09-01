for _ in range(int(input())):
    num = int(input())
    print(
        sum([1 for i in range(2, num + 1, 2)]) +
        sum([1 for i in range(5, num + 1, 5)]) -
        sum([1 for i in range(10, num + 1, 10)])
    )