# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10494 If We Were a Child Again
# ZeroJudge e628


while True:
    try:
        num1, operator, num2 = input().split()
    except EOFError:
        break
    else:
        print(int(num1) // int(num2) if operator == '/' else int(num1) % int(num2))
