# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a057. 正還負呢


from operator import add, sub, mul, truediv

op = (add, sub, mul, truediv)
while True:
    try:
        a, b = map(int, input().split())
    except EOFError:
        break

    if sum(i(a, b) > 0 for i in op) > 2:
        print('Yes!!')
    else:
        print('No...')
