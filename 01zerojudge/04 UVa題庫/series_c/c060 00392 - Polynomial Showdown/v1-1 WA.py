# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00392 Polynomial Showdown
# ZeroJudge c060


from sys import stdin


# length = 9
max_exponent = 8
for line in stdin:
    line = tuple(map(int, line.strip().split()))
    result = [(line[i], max_exponent - i) for i in range(9) if line[i] != 0]
    result = ' + '.join(
        f'{i}{"" if j == 0 else "x" if j == 1 else f"x^{j}"}'
        for i, j in result
    )
    result = result.replace('+ -', '- ').replace('1x', 'x')
    print(result)

# 會誤將 111x 這種格式的結果取代為 11x
