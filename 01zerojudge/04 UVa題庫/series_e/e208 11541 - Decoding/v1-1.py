# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11541 Decoding
# ZeroJudge e208

from re import findall


for case in range(1, int(input()) + 1):
    code = findall(r'\d+|\D', input().rstrip())

    result = [code[idx] * int(code[idx + 1]) for idx in range(0, len(code), 2)]
    
    print(f'Case {case}: {"".join(result)}')
