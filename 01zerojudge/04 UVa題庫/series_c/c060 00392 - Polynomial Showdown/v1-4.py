# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00392 Polynomial Showdown
# ZeroJudge c060


from sys import stdin


# length = 9
max_exponent = 8
for line in stdin:
    line = tuple(map(int, reversed(line.rstrip().split())))
    result = [
        f'{"" if line[i] == 1 and i != 0 else "-" if line[i] == -1 and i != 0 else line[i]}'
        f'{"" if i == 0 else "x"}'
        f'{"" if i in (0, 1) else f"^{i}"}'
        for i in range(9)
        if line[i] != 0
    ]
    result = ' + '.join(reversed(result)).replace('+ -', '- ')
    print(result if result else '0')
