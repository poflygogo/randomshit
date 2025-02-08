# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00392 Polynomial Showdown
# ZeroJudge c060


from sys import stdin


# length = 9
max_exponent = 8
for line in stdin:
    line = tuple(map(int, line.rstrip().split()))
    result = [
        f'{"" if line[i] == 1 and 8 - i != 0 else "-" if line[i] == -1 and 8 - i != 0 else line[i]}'
        f'{"x" if 8 - i != 0 else ""}'
        f'{"" if 8 - i in (0, 1) else f"^{8 - i}"}'
        for i in range(9)
        if line[i] != 0
    ]
    result = ' + '.join(result).replace('+ -', '- ')
    print(result if result else '0')
