# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a037. 我的妹妹哪有這麼聰明！


from operator import add, sub, mul, truediv


def calc(expr: str) -> float:
    def reset_num():
        nonlocal num
        if not num:
            return
        if '.' in num:
            result.append(float(num))
        else:
            result.append(int(num))
        num = ''

    weight = {'+': 1, '-': 1,
              '*': 2, '/': 2,
              '^': 3}
    operator = {'+': add,
                '-': sub,
                '*': mul,
                '/': truediv,
                '^': pow}
    
    result = []
    stack = []
    num = ''
    for i in expr:
        if i.isdigit() or i == '.':
            num += i
        elif i == '(':
            reset_num()
            stack.append(i)
        elif i == ')':
            reset_num()
            while stack[-1] != '(':
                result.append(operator[stack.pop()](result.pop(-2), result.pop()))
            stack.pop()
        else:
            reset_num()
            while stack and stack[-1] != '(' and weight[i] <= weight[stack[-1]]:
                result.append(operator[stack.pop()](result.pop(-2), result.pop()))
            stack.append(i)
    
    reset_num()
    while stack:
        result.append(operator[stack.pop()](result.pop(-2), result.pop()))
    return result.pop()


def main():
    while True:
        try:
            expr = input()
        except EOFError:
            break
        print(f'{calc(expr):.2f}')


if __name__ == '__main__':
    main()
