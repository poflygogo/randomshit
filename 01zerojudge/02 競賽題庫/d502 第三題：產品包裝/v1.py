from sys import stdin
import math

for data in stdin:
    a, b, c, d = map(int, data.strip().split())
    result = c + d + math.ceil(b / 8)
    a -= c * 37
    if a > 0:
        result += math.ceil(a / 36)
    print(result)