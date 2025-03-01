# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a794. 16. Warning: Graphic Functions!
# HP CodeWars 2008

# ----------------------------------------------------------------
# 模擬使用者在終端機中輸入測資

import sys
import io

test = "f(x)=-7.2*cos( (x + 3) / 4 )"
sys.stdin = io.StringIO(test)

# -----------------------------------------------------------------

from operator import add, sub, mul, truediv
from math import floor, ceil, sin, cos, log10
from re import findall

def operate(expr: list, n: int) -> int:
    """ 對傳入的運算式進行計算。

    args:
        expr (list[int|float|str]): 後序運算式。
        n (int): 整數，代表 x 要傳入的值。

    returns:
        int: 整數，計算結果無條件捨去小數點到整數。

    """
    op1 = {'+': add,
           '-': sub,
           '*': mul,
           '/': truediv,
           '^': pow}
    op2 = {'sin': sin,
           'cos': cos,
           'log': log10}

    stack = []
    for item in expr:
        if isinstance(item, (int, float)):
            stack.append(item)
        elif item == 'x':
            stack.append(n)
        elif item in op1:
            stack.append(op1[item](stack.pop(-2), stack.pop()))
        else:
            stack.append(op2[item](stack.pop()))

    result = stack.pop()
    # 無條件捨去小數點到整數
    return floor(result) if result > 0 else ceil(result)


def infix_to_postfix(expr: list) -> list:
    """ 中序運算式轉後序運算式

    args:
        expr (list[str]): 中序運算式

    returns:
        list[int|float|str]: 後序運算式

    """
    weight = {'+': 1, '-': 1,
              '*': 2, '/': 2,
              '^': 3,
              'cos': 4, 'sin': 4, 'log': 4}
    token = {'cos', 'sin', 'log'}

    stack = []
    result = []

    for item in expr:
        if len(item.split('.')) == 2:
            result.append(float(item))
        elif item.strip('-').isdigit():
            result.append(int(item))
        elif item == 'x':
            result.append(item)
        elif item in token or item == '(':
            stack.append(item)
        elif item == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
            if stack and stack[-1] in token:
                result.append(stack.pop())
        else:
            while stack and stack[-1] != '(' and weight[stack[-1]] >= weight[item]:
                result.append(stack.pop())
            stack.append(item)

    if stack:
        result.extend(list(reversed(stack)))

    return result


def main():
    MAX_ROW = 21
    MAX_COL = 21
    MID_ROW = MAX_ROW // 2
    MID_COL = MAX_COL // 2

    # 正規表達式規則: 左至右分別為:
    # 字串開頭的負浮點數 | 字串開頭的負整數 | +-*/()^ | 小數 | 整數 | sin, cos, log
    PATTERN = r'^\-\d+\.\d+|^\-\d+|[\+\-\*\/()\^]|\d+\.\d+|\d+|\w+'

    while True:
        try:
            text = input().replace('f(x)=', '').strip()
        except EOFError:
            break

        # initialize
        graph = [['.'] * MAX_COL for _ in range(MAX_ROW)]
        graph[MID_ROW] = ['-'] * MAX_COL
        for i in range(MAX_ROW):
            graph[i][MID_COL] = '|'
        graph[MID_ROW][MID_COL] = '+'

        # operate expression
        expr = findall(PATTERN, text)
        expr = infix_to_postfix(expr)
        for x in range(-10, 11):
            y = operate(expr, x)

            # draw graph
            if -MID_ROW <= y <= MID_ROW:
                graph[-y + MID_ROW][x + MID_COL] = '*'

        # output
        print('\n'.join(''.join(i) for i in graph))


if __name__ == '__main__':
    main()
