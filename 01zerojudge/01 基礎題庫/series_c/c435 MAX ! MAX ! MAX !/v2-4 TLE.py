length = int(input())
data = tuple(map(int, input().split()))
ans = 0
for i in range(length - 1):
    for j in range(1 + 1, length):
        ans = max(ans, data[i] - data[j])

print(ans)
