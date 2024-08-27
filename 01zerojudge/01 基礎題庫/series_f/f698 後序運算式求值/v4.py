operate = {
    '+': lambda a, b: b + a,
    '-': lambda a, b: b - a,
    '*': lambda a, b: b * a,
    '/': lambda a, b: b // a 
}

data = input().split()
stack = []
for item in data:
    if item in '+-*/':
        stack.append(
            operate[item](stack.pop(-1), stack.pop(-1))
        )
    else:
        stack.append(int(item))

print(int(stack[0]))