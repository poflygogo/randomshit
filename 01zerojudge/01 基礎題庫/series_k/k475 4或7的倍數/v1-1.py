import re
from sys import stdin


a, b, out = input().split()
a, b = int(a), int(b)

for line in stdin:
    numbers = [int(i) for i in re.findall(r'\d+', line)]
    count = sum(i % a == 0 or i % b == 0 or str(a) in str(i) or str(b) in str(i) for i in numbers)
    print(out * count)
