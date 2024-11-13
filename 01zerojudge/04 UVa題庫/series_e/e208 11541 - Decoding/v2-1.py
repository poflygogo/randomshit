# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11541 Decoding
# ZeroJudge e208


for case in range(1, int(input()) + 1):
    code = input().rstrip()

    result = []
    curr_text = ''
    curr_count = 0
    
    for char in code:
        if char.isdigit():
            curr_count *= 10
            curr_count += int(char)
        
        else:
            result.append(curr_text * curr_count)
            curr_text = char
            curr_count = 0
    result.append(curr_text * curr_count)
    
    print(f'Case {case}: {"".join(result)}')
