def f(x: int) -> int:
    return 2 * x - 3


def g(x: int, y: int) -> int:
    return 2 * x + y - 7


def h(x: int, y: int, z: int) -> int:
    return 3 * x - 2 * y + z


stack = []
for item in reversed(input().split()):
    if item not in 'fgh':
        stack.append(int(item))

    elif item == 'f':
        stack.append(f(stack.pop()))

    elif item == 'g':
        stack.append(g(stack.pop(), stack.pop()))

    else:
        stack.append(h(stack.pop(), stack.pop(), stack.pop()))

print(stack[0])
