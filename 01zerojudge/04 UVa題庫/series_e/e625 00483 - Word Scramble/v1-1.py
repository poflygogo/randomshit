# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00483 Word Scramble
# ZeroJudge e625


while True:
    try:
        text = input().split()
    except EOFError:
        break
    else:
        print(' '.join(i[::-1] for i in text))
