num, diff = map(int, input().split())
count, total = 0, 0
for _ in range(num):
    data = [int(i) for i in input().split()]
    if max(data) - min(data) >= diff:
        count += 1
        total += sum(data) // 3
print(count, total)