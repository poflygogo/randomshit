length = int(input())
data = list(map(int, input().split()))
count = 0
for i in range(length - 1, 0, -1):
    for j in range(i):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
            count += 1
print(count)