from collections import Counter


stone = Counter(input().split())
print(max(stone, key=lambda x: stone[x] % 3))
