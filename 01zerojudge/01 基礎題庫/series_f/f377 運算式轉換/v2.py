from sys import stdin, stdout
from collections import deque

weight = {
    '+':1, '-':1, '*':2,
    '/':2, '(':3, ')':0
}

for line in stdin:
    line = line.strip().split()

    result, stack = [], deque()
    for item in line:

        if item in ('+', '-', '*', '/'):
            while stack and weight[item] <= weight[stack[-1]] and stack[-1] != '(':
                result.append(stack.pop())
            stack.append(item)

        elif item == '(':
            stack.append(item)

        elif item == ')':
            toptoken = stack.pop()
            while toptoken != '(':
                result.append(toptoken)
                toptoken = stack.pop()

        else:
            result.append(item)
    
    stack.reverse()
    result.extend(stack)

    stdout.write(f'{" ".join(result)}\n')