# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e394. 許蓋功問題


while True:
    try:
        text = input().rstrip()
    
    except EOFError:
        exit()
    
    else:
        flag = False
        for char in text:
            char_big5 = char.encode('big5').hex()
            if len(char_big5) > 2 and char_big5[-2:] == '5c':
                flag = True
                break
        
        print('Yes' if flag else 'No')
