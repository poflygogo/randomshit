length = int(input())
data = input().split()

result = []
temp_max = int(data.pop(0))
temp_min = temp_max
for i in data:
    i = int(i)
    if i > temp_max:
        result.append(temp_max - temp_min)
        temp_min = temp_max = i
    elif i < temp_min:
        temp_min = i
else:
    result.append(temp_max - temp_min)

print(max(result))
