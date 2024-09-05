_ = input()
data = list(map(int, input().split()))

data.sort()
print(*data)

bad = tuple(filter(lambda x: x < 60, data))
print(max(bad) if bad else 'best case')

good = tuple(filter(lambda x: x >= 60, data))
print(min(good) if good else 'worst case')