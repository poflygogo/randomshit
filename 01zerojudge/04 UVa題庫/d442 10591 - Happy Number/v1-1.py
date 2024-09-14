for i in range(1, int(input()) + 1):
    num = int(input())
    data = []
    while num not in data and 1 not in data:
        data.append(num)
        check = []
        while num > 0:
            check.append((num % 10) ** 2)
            num //= 10
        num = sum(check)
    print(f'Case #{i}: {data[0]} is {"a Happy" if data[-1] == 1 else "an Unhappy"} number.')
