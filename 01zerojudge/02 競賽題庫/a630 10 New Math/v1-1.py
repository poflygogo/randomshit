# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a630. 10. New Math
# HP CodeWars 2007


weight = {'+': 1, '-': 1, '*': 2}
calculate = {
    '+': int.__add__,
    '-': int.__rsub__,
    '*': int.__mul__
}

while True:
    try:
        expr = input().rstrip()
    
    except EOFError:
        break
    
    else:
        expr = expr.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('=^', ' ').split()
        base = int(expr.pop())

        # 計算運算式的值
        num, stack = [], []
        for item in expr:
            if item not in {'+', '-', '*'}:
                item = item.split('^')
                num.append(int(item[0], base=int(item[1])))
            
            else:
                while stack and weight[item] <= weight[stack[-1]]:
                    num.append(calculate[stack.pop()](num.pop(), num.pop()))
                stack.append(item)
        
        while stack:
            num.append(calculate[stack.pop()](num.pop(), num.pop()))
        
        # 確認 num 的正負值
        num = num[0]
        if num >= 0:
            flag = ''
        else:
            flag = '-'
            num = abs(num)
        
        # 根據題目給的條件轉換進位制
        result = []
        while num > 0:
            result.append(num % base)
            num //= base
        
        if result:
            print(f'{flag}{"".join(str(result[i]) if result[i] < 10 else chr(result[i] + 87) for i in range(len(result) - 1, -1, -1))}^{base}')
        
        else:
            print(f'0^{base}')
