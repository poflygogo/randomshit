# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11398 The Base-1 Number System
# ZeroJudge a467


def base1_to_base10(base1: str) -> int:
    base1 = base1.split()
    base2 = []
    flag  = '0'
    for i in base1:
        length = len(i)
        if length == 1:
            flag = '1'
        elif length == 2:
            flag = '0'
        else:
            base2.extend([flag] * (length - 2))
    base2 = ''.join(base2) if base2 else '0'
    return int(base2, 2)


def main():
    while True:
        base1 = input()
        if base1 == '~':
            break
        while base1[-1] != '#':
            base1 += input()
        print(base1_to_base10(base1.strip('#')))


if __name__ == '__main__':
    main()
