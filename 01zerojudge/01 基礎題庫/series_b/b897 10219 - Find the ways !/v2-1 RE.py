import math
from sys import stdin


for line in stdin:
    a, b = map(int, line.strip().split())

    if b == 1:
        print(len(str(a)))
    elif a == b:
        print(1)
    else:
        print(
            int(math.log(math.comb(a, b), 10)) + 1
        )
