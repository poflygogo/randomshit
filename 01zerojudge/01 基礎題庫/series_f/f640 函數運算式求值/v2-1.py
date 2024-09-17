def prefix_expr(item: iter) -> int:
    def operate():
        token = next(item)
        if token == 'f':
            x = operate()
            return 2 * x - 3
        elif token == 'g':
            x = operate()
            y = operate()
            return 2 * x + y - 7
        elif token == 'h':
            x = operate()
            y = operate()
            z = operate()
            return 3 * x - 2 * y + z
        else:
            return int(token)
    return operate()


print(prefix_expr(iter(input().split())))
