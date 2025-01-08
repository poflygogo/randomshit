# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10361 Automatic Poetry
# ZeroJudge m273


import re


for _ in range(int(input())):
    line1 = re.split(r'[<|>]', input().rstrip())
    line2 = input().rstrip().rstrip('.')

    print(''.join(line1))
    print(line2 + line1[3] + line1[2] + line1[1] + line1[4])
