# -*- encoding: utf-8 -*-
# python 3.12
# UVa 13171 Pixel Art
# ZeroJudge i860


from collections import Counter

for _ in range(int(input())):
    remain = input().split()
    require = Counter(remain.pop())
    require['W'] = 0
    remain = {i :int(j) for i, j in zip('MYC', remain)}
    for i in require:
        if i == 'B':
            t = min(*remain.values(), require[i])
            for j in remain:
                remain[j] -= t
        elif i == 'G':
            t = min(remain['Y'], remain['C'], require[i])
            remain['Y'] -= t
            remain['C'] -= t
        elif i == 'R':
            t = min(remain['M'], remain['Y'], require[i])
            remain['M'] -= t
            remain['Y'] -= t
        elif i == 'V':
            t = min(remain['M'], remain['C'], require[i])
            remain['M'] -= t
            remain['C'] -= t
        elif i == 'W':
            continue
        else:
            t = min(remain[i], require[i])
            remain[i] -= t
        require[i] -= t
    
    if any(require.values()):
        print('NO')
    else:
        print('YES', *[remain[i] for i in 'MYC'])
