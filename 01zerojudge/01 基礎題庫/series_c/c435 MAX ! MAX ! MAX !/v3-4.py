input()
data = [int(i) for i in input().split()]

result = 0
temp_max = data.pop(0)
temp_min = temp_max
for i in data:
    if i > temp_max:
        result = max(result, temp_max - temp_min)
        temp_min = temp_max = i
    elif i < temp_min:
        temp_min = i
else:
    result = max(result, temp_max - temp_min)

print(result)
