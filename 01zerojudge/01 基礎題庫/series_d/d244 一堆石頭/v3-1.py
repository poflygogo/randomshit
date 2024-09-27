from collections import Counter


stone = Counter(input().split())
print(min(stone, key=lambda x: stone[x]))
