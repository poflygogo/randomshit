from sys import stdin
from collections import Counter


stdin.readline()
for _ in stdin:
    data = stdin.readline().rstrip().split()
    counter = Counter(data)
    print('Yes' if max(counter.values()) <= len(data) // 2 else 'No')
