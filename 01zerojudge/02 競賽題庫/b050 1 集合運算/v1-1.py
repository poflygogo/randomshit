# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b050. 1. 集合運算
# 96學年度高雄市資訊學科能力競賽

# ---------------------------------

import sys
import io
Q = """2
abcdef
cfehi
2
34abcef
34
0
"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------

FIR_CHR = ord('A')
CONTAIN = ('does not contain', 'contains')
t = 1
n = int(input())
while n:
    groups = [set(input()) for _ in range(n)]
    
    print(f'Test Case {t}:',
          '\n'.join(f'{chr(FIR_CHR + i)}: {{{"".join(map(str, sorted(groups[i])))}}}' for i in range(n)),
          sep='\n')
    
    for i in range(n):
        a = chr(FIR_CHR + i)
        for j in range(i + 1, n):
            b = chr(FIR_CHR + j)
            print(f'{a}+{b}: {{{"".join(map(str, sorted(groups[i].union(groups[j]))))}}}',
                  f'{a}*{b}: {{{"".join(map(str, sorted(groups[i].intersection(groups[j]))))}}}',
                  f'{a}-{b}: {{{"".join(map(str, sorted(groups[i].difference(groups[j]))))}}}',
                  f'{b}-{a}: {{{"".join(map(str, sorted(groups[j].difference(groups[i]))))}}}',
                  f'{a} {CONTAIN[groups[i] >= groups[j]]} {b}',
                  f'{b} {CONTAIN[groups[j] >= groups[i]]} {a}',
                  sep='\n')
    t += 1
    n = int(input())
