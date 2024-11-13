from collections import Counter
from sys import stdin


for line in stdin:
    line = line.rstrip()

    counter = Counter(line)
    for key in sorted(counter, key=lambda x: (counter[x], -ord(x))):
        print(ord(key), counter[key])
