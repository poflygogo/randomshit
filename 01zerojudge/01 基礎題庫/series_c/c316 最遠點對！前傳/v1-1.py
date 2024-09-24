length = int(input())
data = [tuple(map(int, input().split())) for _ in range(length)]

max_len = 0
result = (0, 0)
for i in range(length):
    for j in range(i + 1, length):
        temp = (data[i][0] - data[j][0]) ** 2 + (data[i][1] - data[j][1]) ** 2
        if temp > max_len:
            max_len = temp
            result = (i, j)
print(*result)
