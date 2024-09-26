from itertools import permutations
from collections import ChainMap            # ChainMap 用來合併 dict，但其實也可以用 dict.update()，甚至不合併(我覺得可讀性較差)


default = {'N': 0, 'E': 5, 'O': 9, 'I': 1}  # 很明顯的答案，就直接設固定的值
char = ['F', 'R', 'T', 'Y', 'S', 'X']       # 這樣就從 10! 種狀況減少到 6! 種
for i in permutations(char):
    ans = ChainMap(default, {i:j for i, j in zip(i, (2, 3, 4, 6, 7, 8))})

    # 這邊看不懂的話去看 README，都寫在那邊了
    if ans['F'] + 1 != ans['S'] or \
        (ans['R'] + ans['T'] * 2 + 1) % 10 != ans['X']:
        continue

    forty = sum((ans['F'] * 10000, ans['O'] * 1000, ans['R'] * 100, ans['T'] * 10, ans['Y']))
    ten = sum((ans['T'] * 100, ans['E'] * 10, ans['N']))
    sixty = sum((ans['S'] * 10000, ans['I'] * 1000, ans['X'] * 100, ans['T'] * 10, ans['Y']))

    if forty + ten * 2 == sixty:
        print(f'{forty} + {ten} + {ten} = {sixty}')
        break
