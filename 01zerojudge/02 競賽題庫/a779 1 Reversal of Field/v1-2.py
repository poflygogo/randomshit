# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a779. 1. Reversal of Field
# HP CodeWars 2008


while True:
    try:
        text = input().strip()
    
    except EOFError:
        break

    else:
        print(text)
        text_alpha = ''.join(i.lower() if i.isalnum() else '' for i in text)
        
        if text_alpha == text_alpha[::-1]:
            print('-- is a palindrome')
        else:
            print('-- is not a palindrome')
