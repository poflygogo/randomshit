# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10922 2 the 9s
# ZeroJudge d672


def is_div_by_9(n: int, degree: int=1):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    temp = sum(digits)
    if temp == 9:
        return True, degree
    if temp < 10:
        return False, degree
    return is_div_by_9(temp, degree + 1)


while True:
    num = int(input())
    if not num:
        exit()  

    flag, nine_degree = is_div_by_9(num)
    if flag:
        print(f'{num} is a multiple of 9 and has 9-degree {nine_degree}.')
    else:
        print(f'{num} is not a multiple of 9.')
