from collections import Counter


_ = input()
data = map(int, input().split())
data = Counter(data)
max_time = max(data.values())
for key in sorted(data):
    if data[key] == max_time:
        print(key, max_time)
