data = []
for i in range(7):
    a, b = map(int, input().split())
    data.append(a + b)
result = max(data)
if result <= 8:
    print(0)
else:
    print(data.index(result) + 1)