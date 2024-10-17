input()
data = input().split()
result = []
for i in data:
    if not i in result:
        result.append(i)
print(*result)
