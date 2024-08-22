from sys import stdin

length = int(stdin.readline().strip())
data = tuple(map(int, stdin.readline().split()))

diff = [data[0]]
for idx, item in enumerate(data[1:]):
    diff.append(item - data[idx])

print(*diff)