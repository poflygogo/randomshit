data = tuple(map(int, input().split()))
high = int(input()) + 30
result = 0
for i in data:
    if i <= high:
        result += 1
print(result)