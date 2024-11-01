from sys import stdin
from decimal import Decimal


for line in stdin:
    a, n = map(Decimal, line.rstrip().split())
    
    if a == n == 0:
        print('All Over.')
        exit()
    
    elif a == 0:
        print('0')
    
    elif n == 0:
        print('1')
    
    else:
        print(pow(a, n))
