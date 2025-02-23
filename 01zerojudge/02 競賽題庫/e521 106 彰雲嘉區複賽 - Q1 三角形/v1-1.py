# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e521. 106 彰雲嘉區複賽 - Q1 三角形


for _ in range(int(input())):
    a, b, c = sorted(map(int, input().split()))
    if a + b > c:
        if a == b or a == c or b == c:
            print('1 1')
        else:
            print('1 0')
    else:
        print('0')
