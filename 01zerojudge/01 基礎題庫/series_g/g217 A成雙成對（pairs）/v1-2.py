from sys import stdin
from collections import Counter


for _ in range(int(stdin.readline().rstrip())):
    stdin.readline()
    data = stdin.readline().rstrip().split()
    counter = Counter(data)
    print('Yes' if max(counter.values()) <= len(data) // 2 else 'No')
