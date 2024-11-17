# -*- encoding: utf-8 -*-
# python 3.12
# UVa 01586 Molar mass
# ZeroJudge m042


from re import findall


weight = {'C': 12.01, 'H': 1.008, 'O': 16.00, 'N': 14.01}

for _ in range(int(input())):
    result = 0
    expr = findall(r'\d+|\D', input().rstrip())
    for idx, token in enumerate(expr):
        if token in weight:
            if idx < len(expr) - 1 and expr[idx + 1].isdigit():
                result += weight[token] * int(expr[idx + 1])
            else:
                result += weight[token]
    
    print(f'{result:.3f}')
