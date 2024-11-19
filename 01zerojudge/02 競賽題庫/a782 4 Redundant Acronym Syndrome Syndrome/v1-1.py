# -*- encoding: utf-8 -*-
# python 3.12
# Zerojudge a782
# HP CodeWars 2008


while True:
    text = input().rstrip()
    if text == 'END':
        break

    text = text.split()
    print(''.join(i[0].upper() for i in text), text[-1])
