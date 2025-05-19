# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a017. 五則運算


# ---------------------------------------------------

import sys
import io
Q = """
5 - ( 5 - 2 * 2 ) * 2
"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------


def calc(expr: str, idx: int = 0):
    def operate(sign: str, n: int):
        if sign == '+': stack.append(n)
        elif sign == '-': stack.append(-n)
        elif sign == '*': stack.append(stack.pop() * n)
        elif sign == '/': stack.append(stack.pop() // n)
        elif sign == '%': stack.append(stack.pop() % n)

    num, sign, stack = 0, '+', []
    while idx < len(expr):
        if expr[idx].isdigit():
            num = num * 10 + int(expr[idx])
        elif expr[idx] == '(':
            num, idx = calc(expr, idx + 1)
        elif expr[idx] == ')':
            operate(sign, num)
            return sum(stack), idx
        elif expr[idx] in ('+', '-', '*', '/', '%'):
            operate(sign, num)
            num, sign = 0, expr[idx]
        idx += 1

    operate(sign, num)
    return sum(stack)


def main():
    for _ in range(int(input())):
        print(calc(input().rstrip()))


if __name__ == '__main__':
    main()
