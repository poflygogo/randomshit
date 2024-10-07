import math
import sys


i = 1
for n in sys.stdin:
    n = int(n.rstrip())
    if n == -1:
        break

    print(f'Case {i}: {math.ceil(math.log2(n))}')
    i += 1
