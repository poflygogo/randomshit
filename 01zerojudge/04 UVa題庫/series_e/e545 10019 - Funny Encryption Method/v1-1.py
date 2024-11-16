# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10019 Funny Encryption Method
# ZeroJudge e545


for _ in range(int(input())):
    num = input().rstrip()
    b1 = bin(int(num, base=10)).count('1')
    b2 = bin(int(num, base=16)).count('1')

    print(b1, b2)
