length = input()
data = tuple(map(int, input().split()))
diff = []
for idx, item in enumerate(data[:-1]):
    diff.append(item - min(data[idx + 1:]))

print(max(diff))
