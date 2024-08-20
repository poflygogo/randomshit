"""
UVa 374 Big Mod
"""


from sys import stdin

for line in stdin:
    B, P, M = map(int, line.split())
    
    if P == 0:
        print(1)
    elif P == 1:
        print(B % M)
    elif P % 2 == 0:
        print((B ** (P / 2) % M) * (B ** (P / 2) % M) % M)
    else:
        print((B % M) * (B ** (P / 2) % M) % M)