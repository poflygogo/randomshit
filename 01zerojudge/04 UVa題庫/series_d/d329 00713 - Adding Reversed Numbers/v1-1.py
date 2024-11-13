# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00713 Adding Reversed Numbers
# ZeroJudge d329

for _ in range(int(input())):
    print(int(str(sum(map(
            lambda x: int(x[::-1]),
            input().split()
        )))[::-1]
    ))
