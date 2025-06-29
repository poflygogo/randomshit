# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge l228. 數學運算式(1)


def calc(expr: str, op: str):
    lft, rgt = expr.replace('?', op).split('=')
    return e(lft) == e(rgt)


result = {'+': '+ 加', '-': '- 減', '*': '* 乘', '/': '/ 除'}
e = eval    # 我很抱歉，我墮落了，但真的好懶得寫 stack 哈哈
for _ in range(int(input())):
    data = {}
    for _ in range(int(input()) - 1):
        a, b = input().split("等於")
        data[a] = b

    expr = input()
    for i, j in data.items():
        expr = expr.replace(i, j)
    for i in '+-*/':
        if calc(expr, i):
            print(result[i])
            break
