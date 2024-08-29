from collections import deque as Deque
from re import findall

weight = {
    '+':1, '-':1,
    '*':2, '/':2,
    '(':3
}

caculate = {
    '+': int.__add__,
    '-': int.__rsub__,
    '*': int.__mul__,
    '/': int.__rfloordiv__
}

deque = Deque()
for _ in range(int(input())):
    data = findall(r'\d+|\D', input().strip())

    for item in data:
        if item in ('+', '-', '*', '/'):
            while type(deque[-1]) == str and weight[deque[-1]] >= weight[item] and deque[-1] != '(':
                deque.appendleft(caculate[deque.pop()](deque.popleft(), deque.popleft()))
            deque.append(item)

        elif item == '(':
            deque.append(item)

        elif item == ')':
            while deque[-1] != '(':
                deque.appendleft(caculate[deque.pop()](deque.popleft(), deque.popleft()))
            del deque[-1]

        else:
            deque.appendleft(int(item))
    
    while len(deque) > 1:
        deque.appendleft(caculate[deque.pop()](deque.popleft(), deque.popleft()))
    
    print(deque.pop())