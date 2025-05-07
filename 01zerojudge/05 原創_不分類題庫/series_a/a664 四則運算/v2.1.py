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

ans, deque = [], []
for _ in range(int(input())):
    data = input().strip()

    for item in data:
        if item in ('+', '-', '*', '/'):
            while deque and weight[deque[-1]] >= weight[item] and deque[-1] != '(':
                ans.append(caculate[deque.pop()](ans.pop(), ans.pop()))
            deque.append(item)

        elif item == '(':
            deque.append(item)

        elif item == ')':
            while deque[-1] != '(':
                ans.append(caculate[deque.pop()](ans.pop(), ans.pop()))
            del deque[-1]

        else:
            ans.append(int(item))
    
    while deque:
        ans.append(caculate[deque.pop()](ans.pop(), ans.pop()))
    
    print(ans.pop())