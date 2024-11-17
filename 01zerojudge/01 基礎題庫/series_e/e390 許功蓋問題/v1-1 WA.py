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
            'Yes' if ord(text_big5.__str__()[-2]) == 92 else
            'No'
        )

