# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00713 Adding Reversed Numbers
# ZeroJudge d329

def reverse_num(n: int) -> int:
    result = []
    while n > 9:
        result.append(n % 10)
        n //= 10
    result.append(n)
    return sum(j * 10 ** (len(result) - i - 1) for i, j in enumerate(result))


for _ in range(int(input())):
    print(reverse_num(sum(map(lambda x: reverse_num(int(x)), input().split()))))
