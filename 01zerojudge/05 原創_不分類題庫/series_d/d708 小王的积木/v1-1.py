from sys import stdin
from collections import Counter


data = Counter(stdin.readline().strip() for _ in range((int(stdin.readline()) - 1)))
print(max(data, key=lambda x: data[x] % 2))
