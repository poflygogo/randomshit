length = input()
data = tuple(map(int, input().split()))
diff = []
for idx, item in enumerate(data[:-1]):

    num_diff = 0
    for j in data[idx+1:]:
        if item - j > num_diff:
            num_diff = item - j
    diff.append(num_diff)

print(max(diff))
