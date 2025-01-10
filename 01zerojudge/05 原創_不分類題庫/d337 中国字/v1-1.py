# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d337. 中国字


import unicodedata as ud


while True:
    try:
        text = input()
    except EOFError:
        break

    print(''.join(i for i in text if ud.name(i).startswith('CJK')))
