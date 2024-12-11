# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11878 Homework Checker
# ZeroJudge e659


def mainloop():
    cnt = 0
    while True:
        try:
            expr = input()
        except EOFError:
            print(cnt)
            break
        else:
            if is_correct(expr):
                cnt += 1


def is_correct(expr: str) -> bool:
    if expr[-1] == '?':
        return False
    expr = expr.replace('=', ' = ').replace('+', ' + ').replace('-', ' - ').split()
    if expr[1] == '+' and int(expr[0]) + int(expr[2]) == int(expr[4]):
        return True
    if expr[1] == '-' and int(expr[0]) - int(expr[2]) == int(expr[4]):
        return True
    return False


mainloop()
