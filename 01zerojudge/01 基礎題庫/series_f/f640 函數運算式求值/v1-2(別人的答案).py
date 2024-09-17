def f(x: int) -> int:
    return 2 * x - 3


def g(x: int, y: int) -> int:
    return 2 * x + y - 7


def h(x: int, y: int, z: int) -> int:
    return 3 * x - 2 * y + z


stack = []
for item in reversed(input().split()):
    stack.append(
        f(stack.pop()) if item == 'f'
        else g(stack.pop(), stack.pop()) if item == 'g'
        else h(stack.pop(), stack.pop(), stack.pop()) if item == 'h'
        else int(item)
    )

print(stack[0])
