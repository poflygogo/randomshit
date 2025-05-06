# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a687. 軍方密碼


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
    for i in range(len(num1) - 1, -1, -1):
        d = g_to_int[num1[i]] + g_to_int[num2[i]] + flag
        flag, d = divmod(d, 26)
        result.append(int_to_g[d])
    if flag:
        result.append('B')
    print(''.join(reversed(result)))
