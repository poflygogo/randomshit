from collections import Counter


input()
data = Counter(input().split())
for i in sorted(data):
    print(i, data[i])
