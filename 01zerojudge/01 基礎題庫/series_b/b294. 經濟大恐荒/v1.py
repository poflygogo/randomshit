days = [i for i in range(1, int(input()) + 1)]
cost = tuple(map(int, input().split()))

print(sum(days[i] * num for i, num in enumerate(cost)))
