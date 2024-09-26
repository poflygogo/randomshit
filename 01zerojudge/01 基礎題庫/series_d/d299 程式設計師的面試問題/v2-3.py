from itertools import permutations
from collections import ChainMap


default = {'N': 0, 'E': 5, 'O': 9, 'I': 1}
char = ['F', 'R', 'T', 'Y', 'S', 'X']
for i in permutations(char):
    ans = ChainMap(default, {i:j for i, j in zip(i, (2, 3, 4, 6, 7, 8))})
    if ans['F'] + 1 != ans['S'] or \
        (ans['R'] + ans['T'] * 2 + 1) % 10 != ans['X']:
        continue

    forty = sum((ans['F'] * 10000, ans['O'] * 1000, ans['R'] * 100, ans['T'] * 10, ans['Y']))
    ten = sum((ans['T'] * 100, ans['E'] * 10, ans['N']))
    sixty = sum((ans['S'] * 10000, ans['I'] * 1000, ans['X'] * 100, ans['T'] * 10, ans['Y']))

    if forty + ten * 2 == sixty:
        print(f'{forty} + {ten} + {ten} = {sixty}')
        break
