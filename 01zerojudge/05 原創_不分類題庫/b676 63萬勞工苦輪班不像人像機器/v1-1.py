# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b676. 63萬勞工苦輪班不像人像機器


while True:
    try:
        n = int(input())
    except EOFError:
        exit()
    else:
        print('UGYTI'[n % 5])
