# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10268 198-bis
# ZeroJudge f444


def mainloop():
    from sys import stdin
    for x in stdin:
        x = int(x.rstrip())
        expr = list(map(int, next(stdin).rstrip().split()))

        # Horner's method for derivative
        length = len(expr)
        result = 0
        for i in range(length - 1):
            result = result * x + expr[i] * (length - i - 1)
        print(result)


mainloop()
