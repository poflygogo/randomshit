import math
import sys


i = 1
for n in sys.stdin:
    n = int(n.rstrip())
    if n < 0:
        break

    print(
        f'Case {i}: {math.ceil(math.log(n, 2)) if n != 0 else 0}'
    )
    i += 1
