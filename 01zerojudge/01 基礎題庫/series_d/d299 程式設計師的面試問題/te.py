from itertools import permutations


char = ['F', 'O', 'R', 'T', 'Y', 'E', 'N', 'S', 'I', 'X']
for i in permutations(char):
    ans = {j:i for i, j in enumerate(i)}
    if ans['F'] == 0 or ans['S'] == 0:
        continue

    forty = sum((ans['F'] * 10000, ans['O'] * 1000, ans['R'] * 100, ans['T'] * 10, ans['Y']))
    ten = sum((ans['T'] * 100, ans['E'] * 10, ans['N']))
    sixty = sum((ans['S'] * 10000, ans['I'] * 1000, ans['X'] * 100, ans['T'] * 10, ans['Y']))

    if forty + ten * 2 == sixty:
        print(f'{forty} + {ten} + {ten} = {sixty}')
