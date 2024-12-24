# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d103. NOIP 2008 1.ISBN号码
# NOIP 2008 普及組 複賽
# 
# 盡管題目說有多行，但實際上只有一行


ISBN_code = input()
ISBN_no_dash = ''.join(i for i in ISBN_code.split('-'))
identifier = sum((i + 1) * int(ISBN_no_dash[i]) for i in range(9)) % 11
identifier = str(identifier) if identifier < 10 else 'X'
if identifier == ISBN_code[-1]:
    print('Right')
else:
    print(ISBN_code[:-1] + identifier)
