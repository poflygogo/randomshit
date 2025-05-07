from collections import deque as Deque

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

for _ in range(int(input())):
    data = input().strip()

    deque = Deque()
    for item in data:
        if item in '+-*/':
            while weight[deque[-1]] <= weight[item] and deque[-1] != '(':
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
    
    print(deque.pop())