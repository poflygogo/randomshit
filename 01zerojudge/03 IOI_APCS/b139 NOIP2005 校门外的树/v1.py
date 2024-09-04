length, m = map(int, input().split())
data = [True for _ in range(length + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        data[i] = False
print(sum(data))