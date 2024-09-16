n = int(input()) - 1
a, b = map(int, input().split())
prev = (a, b)
data = []
for _ in range(n):
    a, b = map(int, input().split())
    data.append(
        abs(prev[0] - a) + abs(prev[1] - b)
    )
    prev = (a, b)

print(max(data), min(data))
