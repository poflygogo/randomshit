# -*- encoding: utf-8 -*-
# python 3.8
# UVa 00530 - Binomial Showdown
# ZeroJudge c061

from math import comb


def main():
    while True:
        a, b = map(int, input().split())
        if a == b == 0:
            break
        print(f"{a} things taken {b} at a time is {comb(a, b)} exactly.")


main()
