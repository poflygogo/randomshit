# -*- encoding: utf-8 -*-
# python 3.12
# UVa 12004 Bubble Sort
# ZeroJudge m298


def main():
    for i in range(1, int(input()) + 1):
        print(f'Case {i}: {average_swap(int(input()))}')


def average_swap(n: int) -> str:
    n *= n - 1
    if n % 4 == 0:
        return str(n // 4)
    return f'{n // 2}/2'


main()
