from sys import stdin
from itertools import product


for num in stdin:
    for i in product(['0', '1'], repeat=int(num)):
        print(*i, sep='')
