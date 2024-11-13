# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10922 2 the 9s
# ZeroJudge d672


def is_div_by_9(n: str, degree: int=1):
    temp = sum(map(int, n))
    if temp == 9:
        return True, degree
    if temp < 10:
        return False, degree
    return is_div_by_9(str(temp), degree + 1)


while True:
    num = input().rstrip()
    if num == '0':
        exit()  

    flag, nine_degree = is_div_by_9(num)
    if flag:
        print(f'{num} is a multiple of 9 and has 9-degree {nine_degree}.')
    else:
        print(f'{num} is not a multiple of 9.')
