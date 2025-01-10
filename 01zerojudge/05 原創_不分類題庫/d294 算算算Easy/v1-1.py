# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d294. 算算算....Easy


def comb(a: int, b: int) -> int:
    return a * (a + 1) * b * (b + 1) // 4


def main():
    while True:
        try:
            print(comb(*sorted(map(int, input().split()))))
        except EOFError:
            break


main()
