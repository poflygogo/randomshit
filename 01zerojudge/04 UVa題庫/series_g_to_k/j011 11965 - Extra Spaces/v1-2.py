# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11965 Extra Spaces
# ZeroJudge j011


for t in range(1, int(input()) + 1):
    print(f'Case {t}:')
    for _ in range(int(input())):
        text = input()
        while '  ' in text:
            text = text.replace('  ', ' ')
        print(text)
