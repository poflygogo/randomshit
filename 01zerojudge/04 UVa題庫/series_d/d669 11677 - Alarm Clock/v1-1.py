# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11677 Alarm Clock
# ZeroJudge d669

while True:
    h1, m1, h2, m2 = map(int, input().split())
    if h1 == m1 == h2 == m2 == 0:
        exit()
    
    print((h2 * 60 + m2 - h1 * 60 - m1 + 1440) % 1440)
