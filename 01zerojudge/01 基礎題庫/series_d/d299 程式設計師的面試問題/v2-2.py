from itertools import permutations


char = ['F', 'O', 'R', 'T', 'Y', 'E', 'N', 'S', 'I', 'X']   # 把所有元素都放到一個長度為 10 的 list 中
for i in permutations(char):                                # 直接對其進行排列組合，暴搜，窮舉
    ans = {j:i for i, j in enumerate(i)}                    # 用字典生成式建立對照表
    if ans['F'] == 0 or \
        ans['S'] == 0 or \
        ans['N'] != 0 or \
        ans['E'] != 5 or \
        ans['I'] != 1 or \
        ans['O'] != 9 or \
        ans['F'] + 1 != ans['S'] or \
        (ans['R'] + ans['T'] * 2 + 1) % 10 != ans['X']:
        continue

    forty = sum((ans['F'] * 10000, ans['O'] * 1000, ans['R'] * 100, ans['T'] * 10, ans['Y']))
    ten = sum((ans['T'] * 100, ans['E'] * 10, ans['N']))
    sixty = sum((ans['S'] * 10000, ans['I'] * 1000, ans['X'] * 100, ans['T'] * 10, ans['Y']))

    if forty + ten * 2 == sixty:
        print(f'{forty} + {ten} + {ten} = {sixty}')
        break
