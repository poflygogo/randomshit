from sys import stdin, stdout
from collections import deque


def operate(operator:str, num1:int, num2:int):
    if operator == '+':
        return num2 + num1
    if operator == '-':
        return num2 - num1
    if operator == '*':
        return num2 * num1
    if operator == '/':
        return num2 / num1


data = stdin.readline().strip().split()

stack = deque()
for item in data:
    if item in '+-*/':
        stack.append(
            operate(item, stack.pop(), stack.pop())
        )
    else:
        stack.append(int(item))

stdout.write(f'{int(stack[0])}')