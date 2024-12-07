# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10340 All in All
# ZeroJudge e624


while True:
    try:
        str_s, str_t = input().split()
    except EOFError:
        break
    else:
        length = len(str_s)
        idx = 0
        for chr in str_t:
            if chr == str_s[idx]:
                idx += 1
                if idx == length:
                    print('Yes')
                    break
        else:
            print('No')
