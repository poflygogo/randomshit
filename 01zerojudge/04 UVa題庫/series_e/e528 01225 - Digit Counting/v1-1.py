# -*- encoding: utf-8 -*-
# python 3.12
# UVa 01225 Digit Counting
# ZeroJudge e528


def main():
    for _ in range(int(input())):
        print(*digit_count(int(input())))


def digit_count(n: int) -> list:
    counter = [0] * 10
    for i in range(1, n + 1):
        while i > 0:
            counter[i % 10] += 1
            i //= 10
    return counter


main()
