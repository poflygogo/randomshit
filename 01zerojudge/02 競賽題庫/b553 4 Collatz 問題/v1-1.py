# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge b553
# 103學年度北二區桃竹苗基區資訊學科能力競賽


while True:
    try:
        n = input()
        if n == '':
            continue
        n = int(n)
    
    except EOFError:
        break

    else:
        t = 0
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n = n * 3 + 1
            t += 1
        
        print(t)
