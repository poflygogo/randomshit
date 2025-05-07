# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d137. 绝对值


while True:
    try:
        n = complex(input().replace('i', 'j'))
    except EOFError:
        break
    print(f'{abs(n):.3f}')
