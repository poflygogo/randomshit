# -*- encoding: utf-8 -*-
# python 3.12
# UVa 12372 Packing for Holiday
# ZeroJudge i919


for test_case in range(1, int(input()) + 1):
    print(f'Case {test_case}:', 'good' if all(map(lambda x: int(x) <= 20, input().split())) else 'bad')
