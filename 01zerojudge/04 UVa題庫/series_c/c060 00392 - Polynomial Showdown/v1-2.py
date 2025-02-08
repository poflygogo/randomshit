# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00392 Polynomial Showdown
# ZeroJudge c060


from sys import stdin


# length = 9
max_exponent = 8
for line in stdin:
    line = tuple(map(int, line.strip().split()))
    temp = [(line[i], max_exponent - i) for i in range(9) if line[i] != 0]
    result = []
    for i, j in temp:
        if j == 0:
            result.append(str(i))
        elif j == 1:
            if i == 1:
                result.append('x')
            elif i == -1:
                result.append(f'-x')
            else:
                result.append(f'{i}x')
        elif i == 1:
            result.append(f'x^{j}')
        elif i == -1:
            result.append(f'-x^{j}')
        else:
            result.append(f'{i}x^{j}')

    result = ' + '.join(result).replace('+ -', '- ')
    print(result if result else '0')


# 笑死好多 if
