from sys import stdin, stdout
from collections import deque

weight = {
    '+':1, '-':1,
    '*':2, '/':2, '%':2,
    '(':3
}

caculate = {
    '+': int.__add__,           # 加法
    '-': int.__rsub__,          # 減法, 後面 - 前面
    '*': int.__mul__,           # 乘法
    '/': int.__rfloordiv__,     # 除法, 後面 // 前面
    '%': int.__rmod__           # 求餘, 後面 % 前面
}

for expression in stdin:
    expression = expression.strip().split()
    postfix, stack = [], deque()

    # 轉換成後序表達式
    for item in expression:
        if item in '+-*/%':
            while stack and weight[item] <= weight[stack[-1]] and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.append(item)

        elif item == '(':
            stack.append(item)

        elif item == ')':
            topitem = stack.pop()
            while topitem != '(':
                postfix.append(topitem)
                topitem = stack.pop()

        else:
            postfix.append(int(item))
    
    stack.reverse()
    postfix.extend(stack)

    # 對後序表達式進行計算
    stack.clear()
    for item in postfix:
        if type(item) is str:
            stack.append(
                caculate[item](stack.pop(), stack.pop())
            )
        else:
            stack.append(item)
    
    stdout.write(f'{stack.pop()}\n')