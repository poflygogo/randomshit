from sys import stdin, stdout
from itertools import product


cac = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)
pre_cac = {}
for a, b, c, d in product(range(10), range(10), range(10), range(10)):
    pre_cac[f'{a}{b}{c}{d}'] = sum((cac[a], cac[c], b, d))

stdin.readline()
for line in stdin:
    result = sum(map(lambda x: pre_cac[x], line.rstrip().split()))
    stdout.write('Valid\n' if not result % 10 else 'Invalid\n')


# AC (3.9s, 4.5MB)
# zerojudge a159
# UVa 11743
# 2024-10-19
