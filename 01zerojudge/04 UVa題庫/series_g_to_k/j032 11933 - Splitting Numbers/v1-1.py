# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11933 Splitting Numbers
# ZeroJudge j032


n = int(input())
while n:
    n = bin(n)[2:]
    a = ['0'] * len(n)
    b = a.copy()
    flag = True
    for i, j in enumerate(reversed(n)):
        if j == '1':
            if flag:
                a[i] = '1'
            else:
                b[i] = '1'
            flag ^= True
    
    print(int(''.join(reversed(a)), base=2),
          int(''.join(reversed(b)), base=2))

    n = int(input())
