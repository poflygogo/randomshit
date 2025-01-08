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
    for i in range(n):
        if arr[i] == '.':
            count += 1
            arr[i] = '#'
            if i < n - 1:
                arr[i + 1] = '#'
                if i < n - 2:
                    arr[i + 2] = '#'
    return count


if __name__ == '__main__':
    main()
