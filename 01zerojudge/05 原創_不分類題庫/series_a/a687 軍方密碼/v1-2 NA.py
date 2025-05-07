# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a687. 軍方密碼


from itertools import zip_longest

int_to_g = {i: chr(i + 65) for i in range(26)}
g_to_int = {chr(i + 65): i for i in range(26)}
while True:
    try:
        input()
    except EOFError:
        break
    num1 = input().rstrip()
    num2 = input().rstrip()

    result = []
    flag = 0
    for a, b in zip_longest(reversed(num1), reversed(num2), fillvalue='A'):
        d = g_to_int[a] + g_to_int[b] + flag
        flag, d = divmod(d, 26)
        result.append(int_to_g[d])
    if flag:
        result.append('B')
    print(''.join(reversed(result)))
