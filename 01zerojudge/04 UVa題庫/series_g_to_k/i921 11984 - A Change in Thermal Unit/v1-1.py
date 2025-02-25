# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11984 A Change in Thermal Unit
# ZeroJudge i921


for test_case in range(1, int(input()) + 1):
    a, b = map(int, input().split())
    print(f'Case {test_case}: {((a * 9 / 5 + 32 + b) - 32) * 5 / 9:.2f}')
