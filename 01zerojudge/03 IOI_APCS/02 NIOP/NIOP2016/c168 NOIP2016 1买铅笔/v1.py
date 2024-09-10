from math import ceil

stu = int(input())
data = []
for _ in range(3):
    a, b = map(int, input().split())
    data.append(ceil(stu / a) * b)
print(min(data))