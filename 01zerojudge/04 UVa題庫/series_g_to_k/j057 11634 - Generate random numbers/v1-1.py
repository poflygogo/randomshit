# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11634 Generate random numbers
# ZeroJudge j057


def main():
    while True:
        n = int(input())
        if n == 0:
            break
        seen = set()
        while n not in seen:
            seen.add(n)
            n **= 2
            n = int(str(n).zfill(8)[2:6])
        print(len(seen))


main()
