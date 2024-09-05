data = set()
for _ in range(int(input())):
    a, b = map(int, input().split())
    data.update({i for i in range(a, b)})

print(len(data))