# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b430. 簡單乘法


while True:
    try:
        a, b, n = map(int, input().split())
    except EOFError:
        break
    print(pow(pow(a, 1, n) * pow(b, 1, n), 1, n))
