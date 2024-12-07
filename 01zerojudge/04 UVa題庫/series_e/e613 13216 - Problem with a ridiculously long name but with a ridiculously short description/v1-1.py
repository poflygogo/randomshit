# -*- encoding: utf-8 -*-
# python 3.12
# UVa 13216 Problem with a ridiculously long name but with a ridiculously short description
# ZeroJudge e613


# pow(66, n, 100) 的值會循環，找尋環節即可
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        print('1')
    elif n == 1:
        print('66')
    else:
        print((16, 56, 96, 36, 76)[(n - 1) % 5])
