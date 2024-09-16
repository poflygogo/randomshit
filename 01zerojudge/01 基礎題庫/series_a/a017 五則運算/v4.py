from sys import stdin, stdout

weight = {
    '+':1, '-':1,
    '*':2, '/':2, '%':2,
    '(':3
}

caculate = {
    '+': int.__add__,           # 加法
    '-': int.__rsub__,          # 減法, 後面 - 前面
    '*': int.__mul__,           # 乘法
    '/': int.__rfloordiv__,     # 除法, 後面 // 前面
    '%': int.__rmod__           # 求餘, 後面 % 前面
}

result, symbol = [], []

for expression in stdin:
    expression = expression.split()
    
    # 一邊轉換成後序表達式，一邊進行運算
    for item in expression:
        if item in '+-*/%':
            while symbol and weight[item] <= weight[symbol[-1]] and symbol[-1] != '(':
                result.append(
                    caculate[symbol.pop()](result.pop(), result.pop())
                    )
            symbol.append(item)

        elif item == '(':
            symbol.append(item)

        elif item == ')':
            topitem = symbol.pop()
            while topitem != '(':
                result.append(
                    caculate[topitem](result.pop(), result.pop())
                )
                topitem = symbol.pop()

        else:
            result.append(int(item))
    
    while symbol:
        result.append(
            caculate[symbol.pop()](result.pop(), result.pop())
        )
    
    stdout.write(f'{result.pop()}\n')