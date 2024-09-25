length = int(input()) - 1
data = [int(i) for i in input().split()]
data.sort()
print(*data)

while length > 0:
    print(data[length], end=' ')
    length -= data.count(data[length])
print(data[0])
