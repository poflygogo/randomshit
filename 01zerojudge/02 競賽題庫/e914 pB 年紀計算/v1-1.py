# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e914. pB. 年紀計算
# 2019大學學測推甄申請二階


# 18 <= m <= 99
# m = 2(d + n) - n = 2d + n
# m = 10(d % 10) + d // 10

def age_calculator(n: int, min_age: int=18, max_age: int=100):
    for i in range(min_age + n + (n % 2), max_age, 2):
        foo, bar = i // 2 - n, i - n
        if foo > 0 and (10 * (foo % 10) + foo // 10 == bar):
            return foo
    return "no answer"

print(age_calculator(int(input())))
