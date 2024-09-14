for i in range(1, int(input()) + 1):
    num = int(input())
    data = []
    while num not in data and 1 not in data:
        data.append(num)
        num = sum(int(i) ** 2 for i in str(num))
    print(f'Case #{i}: {data[0]} is {"a Happy" if num == 1 else "an Unhappy"} number.')
