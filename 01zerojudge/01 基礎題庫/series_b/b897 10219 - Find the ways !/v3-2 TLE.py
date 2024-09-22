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
                math.log(
                    round(math.sqrt(2 * a * math.pi), 2) * round(a / 3, 2) ** a //
                    round(math.sqrt(2 * b * math.pi), 2) * round(b / 3, 2) ** b //
                    round(math.sqrt(2 * (a - b) * math.pi), 2) * round((a - b) // 3, 2) ** (a - b),
                    10
                )
            ) + 1
        )
