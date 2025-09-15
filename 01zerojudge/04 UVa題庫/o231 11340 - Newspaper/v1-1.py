# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11340 - Newspaper
# ZeroJudge o231


for _ in range(int(input())):
    data = dict((lambda x, y: (x, int(y)))(*input().split()) for _ in range(int(input())))
    result = sum(sum(data.get(i, 0) for i in input().strip()) for _ in range(int(input())))
    print("%.02f$" % (result / 100))
