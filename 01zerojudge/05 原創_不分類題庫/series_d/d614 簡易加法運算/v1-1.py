# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d614. 簡易加法運算


for _ in range(int(input())):
    print(sum(map(int, filter(lambda x: x.isdigit(), input().split()))))
