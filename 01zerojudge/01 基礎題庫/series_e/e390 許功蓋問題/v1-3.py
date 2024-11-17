# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e390. 許功蓋問題


while True:
    try:
        text_unicode = input().rstrip()
    
    except EOFError:
        exit()
    
    else:
        text_big5 = text_unicode.encode('big5')

        print(
            'Yes' if len(text_big5.hex()) > 2 and  text_big5.hex()[-2:] == '5c' else
            'No'
        )

        print(text_big5)
