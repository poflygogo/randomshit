a, b = map(int, input().split())

print(sum(range(a + (a % 2), b + 1, 2)))