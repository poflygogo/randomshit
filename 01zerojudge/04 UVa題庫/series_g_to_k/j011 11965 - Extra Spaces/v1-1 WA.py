# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11965 Extra Spaces
# ZeroJudge j011


for t in range(1, int(input()) + 1):
    print(f'Case {t}:',
          '\n'.join(input().replace('    ', ' ').replace('  ', ' ') for _ in range(int(input()))),
          sep='\n')
