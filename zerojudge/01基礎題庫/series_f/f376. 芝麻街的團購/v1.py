from statistics import median_low

_ = input()
data = tuple(map(int, input().split()))
print(median_low(data))