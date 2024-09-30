from bisect import bisect


length, _ = map(int, input().split())
data = [int(i) for i in input().split()]

for query in (int(i) for i in input().split()):
    idx = bisect(data, query)
    if data[idx - 1] == query:
        print(idx)
    else:
        print(0)
