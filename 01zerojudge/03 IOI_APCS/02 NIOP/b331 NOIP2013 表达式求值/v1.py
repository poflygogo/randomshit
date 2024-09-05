import operator, functools

def mul(expr:str) -> int:
    expr:list = list(map(int, expr.split('*')))
    return functools.reduce(operator.mul, expr)

data = input().split('+')
data = map(mul, data)
print(sum(data) % 10000)