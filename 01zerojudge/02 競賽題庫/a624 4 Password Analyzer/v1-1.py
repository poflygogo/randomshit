# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a624. 4. Password Analyzer
# HP CodeWars 2007


while True:
    try:
        password = input()
    except EOFError:
        break
    else:
        pattern_length = len(password) >= 8
        pattern_low = False
        pattern_upper = False
        pattern_symbol = False
        for i in password:
            if not all((pattern_low, pattern_upper, pattern_symbol)):
                if 65 <= ord(i) <= 90:
                    pattern_upper = True
                
                elif 97 <= ord(i) <= 122:
                    pattern_low = True
                
                else:
                    pattern_symbol = True
            
            else:
                break
        

        result = ['WEAK', 'ACCEPTABLE', 'GOOD', 'STRONG'][sum((
            pattern_length,
            pattern_low and pattern_upper,
            pattern_symbol and (pattern_low or pattern_upper))
            )]
        print(f'This password is {result}')
