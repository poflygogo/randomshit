from collections import Counter
from itertools import takewhile


_ = input()
data = map(int, input().split())
data = Counter(data).most_common()
for i in sorted(takewhile(lambda x: x[1] == data[0][1], data)):
    print(*i)
