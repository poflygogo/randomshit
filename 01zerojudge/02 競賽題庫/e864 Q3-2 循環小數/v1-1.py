# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e864. Q3-2 循環小數
# 108學年度商業類程式設計競賽


# ---------------------------------------------------

import sys
import io
Q = """
3 
76 25 
5 43 
1 397
"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------



def div(a: int, b: int) -> str:
    integer, a = divmod(a, b)
    decimal = []
    reminder = {}
    idx = 0
    while a and a not in reminder:
        reminder[a] = idx
        t, a = divmod(a * 10, b)
        decimal.append(t)
        idx += 1
    
    decimal_a = ''.join(map(str, decimal))
    decimal_b = '0'
    if a != 0:
        decimal_a = ''.join(map(str, decimal_a[:reminder[a]]))
        decimal_b = decimal[reminder[a]:]
        if len(decimal_b) > 50:
            decimal_b = ''.join(map(str, decimal_b[:50])) + '...'
        else:
            decimal_b = ''.join(map(str, decimal_b))

    return f'{integer}.{decimal_a}({decimal_b})'


def main():
    for _ in range(int(input())):
        print(div(*map(int, input().split())))


main()
