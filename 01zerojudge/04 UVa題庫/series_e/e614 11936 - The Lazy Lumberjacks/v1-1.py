# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11936 The Lazy Lumberjacks
# ZeroJudge e614


for _ in range(int(input())):
    a, b, c = sorted(map(int, input().split()))
    print('OK' if a + b > c else 'Wrong!!')
