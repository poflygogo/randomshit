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
        print(
            int(
                sum((math.log(i, 10) for i in range(a, a - b, -1))) -
                sum((math.log(i, 10) for i in range(b, 1, -1)))
            ) + 1
        )
