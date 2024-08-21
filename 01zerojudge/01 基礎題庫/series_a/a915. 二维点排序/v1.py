times = int(input())

data = [tuple(map(int, input().split())) for _ in range(times)]
data = sorted(data, key= lambda n:(n[0], n[1]))

for line in data:
    print(*line)
