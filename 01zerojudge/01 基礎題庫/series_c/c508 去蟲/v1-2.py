input()
data = [int(i) for i in input().split()]
data.sort()
print(*data)

data = list(set(data))
data.sort(reverse=True)
print(*data)
