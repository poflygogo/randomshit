import math, sys

for line in sys.stdin:
    line = line.strip()
    if not line: break
    numA, numB = map(int, line.split())
    print(math.gcd(numA, numB))