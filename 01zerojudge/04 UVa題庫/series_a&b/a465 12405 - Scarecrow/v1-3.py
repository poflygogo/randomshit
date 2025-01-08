# -*- encoding: utf-8 -*-
# python 3.12
# UVa 12405 Scarecrow
# ZeroJudge a465


def main():
    for i in range(1, int(input()) + 1):
        print(f'Case {i}: {uva_scarecrow(int(input()), list(input()))}')


def uva_scarecrow(n: int, arr: list) -> int:
    """
    args:
        n  : length of arr.(0 < n < 100)
        arr: data of field.
    return:
        int, the number of scarecrows that need to be placed.
    """
    count = 0
    i = 0
    while i < n:
        if arr[i] == '.':
            count += 1
            i += 3
        else:
            i += 1
    return count


if __name__ == '__main__':
    main()
