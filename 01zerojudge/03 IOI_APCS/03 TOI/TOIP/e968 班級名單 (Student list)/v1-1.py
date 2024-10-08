n = int(input())
data = tuple(map(int, input().split()))
for i in range(n, 0, -1):
    if i in data:
        continue
    print(f'No. {i}')
