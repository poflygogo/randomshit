data = [int(i) for i in input().split()]
count = 0
temp = []
for i in range(1, len(data) - 1):
    if data[i - 1] < data[i] and data[i + 1] <= data[i]:
        count += 1
else:
    if data[i] == data[i + 1]:
        count -= 1

print(count)
