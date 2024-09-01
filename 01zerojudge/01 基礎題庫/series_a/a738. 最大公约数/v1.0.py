import math, sys

for line in sys.stdin:
    numA, numB = map(int, line.strip().split())
    print(math.gcd(numA, numB))