# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00621 Secret Research
# ZeroJudge e683


for _ in range(int(input())):
    code = input()
    if code in {'1', '4', '78'}:
        print('+')
    elif code == code[:-2] + '35':
        print('-')
    elif code == '9' + code[1:-1] + '4':
        print('*')
    else:
        print('?')
