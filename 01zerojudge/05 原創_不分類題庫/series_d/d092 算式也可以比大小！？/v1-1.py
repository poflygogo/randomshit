# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d092. 算式也可以比大小！？


def get_value(a, b):
    return (2 if a > b else 1 if a == b else 0, a + b)


op = '<=>'
n = int(input())
while n:
    arr = [get_value(*map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda x: (x[1], x[0]), reverse=True)
    print(' '.join(f'{op[i]}{j}' for i, j in arr))
    n = int(input())
