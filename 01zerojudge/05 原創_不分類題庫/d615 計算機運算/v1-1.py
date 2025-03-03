# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d615. 計算機運算


operator = {
    '+': int.__add__,
    '-': int.__sub__,
    '*': int.__mul__,
    '/': int.__floordiv__,
}

for _ in range(int(input())):
    expr = input().split()
    result = int(expr[0])
    for i in range(1, len(expr), 2):
        result = operator[expr[i]](result, int(expr[i + 1])) % 9223372036854775808  # 題目有坑，出題者生測資時發生溢位了
    print(result)
