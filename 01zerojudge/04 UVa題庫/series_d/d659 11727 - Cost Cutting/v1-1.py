# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11727 Cost Cutting
# ZeroJudge d659

for case in range(1, int(input()) + 1):
    print(f'Case {case}: {sorted(input().split(), key=int)[1]}')
    