count = 0
for _ in range(5):
    a, b, c = sorted(map(int, input().split()))
    if (a + b)> c:
        count += 1
print(count)