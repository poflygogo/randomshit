# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e128. 新北100-1貪食蛇
# 北縣新北北三區100年資訊學科能力競賽


from math import sqrt, ceil


def main():
    n = int(input())
    while n:
        print(*snake(n))
        n = int(input())


def snake(n: int):
    cycle = ceil(sqrt(n))
    cycle_end_value = cycle ** 2
    cycle_mid_value = cycle_end_value - cycle + 1
    if n == cycle_end_value:
        x, y = 1, cycle
    elif n == cycle_mid_value:
        x = y = cycle
    elif n < cycle_mid_value:
        x, y = cycle, cycle - (cycle_mid_value - n)
    else:
        x, y = cycle - (n - cycle_mid_value), cycle

    if cycle % 2 == 0:
        x, y = y, x
    return x, y


if __name__ == '__main__':
    main()
