import math
from sys import stdin


for line in stdin:
    a, b = map(int, line.strip().split())
    if b > a - b:
        b = a - b

    if b == 1:
        print(len(str(a)))
    elif a == b:
        print(1)
    else:
        print(int(math.log(
            (int(math.sqrt(2 * a * math.pi) * (a / math.e) ** a) + 1) /
            (int(math.sqrt(2 * b * math.pi) * (b / math.e) ** b) + 1) /
            (int(math.sqrt(2 * (a - b) * math.pi) * ((a - b) / math.e) ** (a - b)) + 1),
            10
            )) + 1
        )
