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
        for j in str(i):
            counter[int(j)] += 1
    return counter


main()
