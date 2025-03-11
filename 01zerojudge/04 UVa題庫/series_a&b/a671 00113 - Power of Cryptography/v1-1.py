# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a671. 00113 - Power of Cryptography


def main():
    while True:
        try:
            a, b = int(input()), int(input())
        except EOFError:
            break
        print(operate(a, b))


def operate(a: int, b: int) -> int:
    return int(round(pow(b, 1 / a), 1))


main()
