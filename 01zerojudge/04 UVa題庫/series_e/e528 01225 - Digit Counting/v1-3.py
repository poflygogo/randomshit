# -*- encoding: utf-8 -*-
# python 3.12
# UVa 01225 Digit Counting
# ZeroJudge e528


def main():
    for _ in range(int(input())):
        print(*digit_count(int(input())))


def digit_count(n: int) -> list:
    from collections import Counter
    count = Counter(''.join(str(i) for i in range(1, n + 1)))
    return [count[str(i)] for i in range(10)]


main()
