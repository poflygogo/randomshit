counter = {}


_ = input()
data = map(int, input().split())
for i in data:
    counter[i] = counter.get(i, 0) + 1
max_count = max(counter.values())
for i in sorted(counter):
    if counter[i] == max_count:
        print(i, max_count)
