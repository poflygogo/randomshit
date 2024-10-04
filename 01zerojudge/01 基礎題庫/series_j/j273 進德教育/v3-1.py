input()
data = {}
for i in input().split():
    data[i] = data.get(i, 0) + 1
for i in sorted(data):
    print(i, data[i])
