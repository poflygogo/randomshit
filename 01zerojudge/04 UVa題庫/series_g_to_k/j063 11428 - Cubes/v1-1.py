# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11428 Cubes
# ZeroJudge j063


limit = 61
cube = [i ** 3 for i in range(limit)]


def func(n):
    for i in range(1, limit):
        for j in range(i + 1, limit):
            if cube[j] - cube[i] == n:
                return f'{j} {i}'
            if cube[j] - cube[i] > n:
                break
    return 'No solution'


n = int(input())
while n:
    print(func(n))
    n = int(input())
