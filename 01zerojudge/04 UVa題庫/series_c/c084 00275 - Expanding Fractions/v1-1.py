# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00275 Expanding Fractions
# ZeroJudge c084


TEXT_REPEAT = 'The last {} digits repeat forever.'
TEXT_NORMAL = 'This expansion terminates.'
a, b = map(int, input().split())
while not a == b == 0:
    decimal = []
    reminder = {}
    idx = 0
    while a and a not in reminder:
        reminder[a] = idx
        t, a = divmod(a * 10, b)
        decimal.append(t)
        idx += 1
    
    result = '.' + ''.join(map(str, decimal))
    print('\n'.join(result[i:i+50] for i in range(0, len(result), 50)))
    print(TEXT_REPEAT.format(len(decimal) - reminder[a]) if a else TEXT_NORMAL)
    a, b = map(int, input().split())
