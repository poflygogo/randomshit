from sys import stdin
from decimal import Decimal
 

for line in stdin:
    a, n = map(Decimal, line.rstrip().split())
    
    if a == n == 0:
        print(f'All Over. Exceeded {len(stdin.readlines())} lines!')
        exit()

    print(pow(a, n))
