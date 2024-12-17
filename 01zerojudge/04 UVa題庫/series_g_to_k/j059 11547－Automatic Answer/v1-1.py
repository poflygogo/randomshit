# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11547 Automatic Answer
# ZeroJudge j059
# 
# 題目給的運算式可以化簡成 315n + 36962
# 這樣就可以避免浮點數運算
# 或者... 315 * (n + 117) + 107


for _ in range(int(input())):
    print(abs(int(input()) * 315 + 36962) // 10 % 10)
