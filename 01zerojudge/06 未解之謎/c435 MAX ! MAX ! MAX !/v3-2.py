length = int(input())
data = [int(i) for i in input().split()]

result = []
temp_max = (0, data[0])
for i in range(1, length):
    if data[i] > temp_max[1]:
        result.append(temp_max[1] - min(data[temp_max[0]: i]))
        temp_max = (i, data[i])
else:
    result.append(temp_max[1] - min(data[temp_max[0]:]))

print(max(result))
