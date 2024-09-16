length = input()
data = tuple(map(int, input().split()))
prefix_sum = [data[0]]

for idx, item in enumerate(data[1:]):
    prefix_sum.append(prefix_sum[idx] + item)

print(*prefix_sum)