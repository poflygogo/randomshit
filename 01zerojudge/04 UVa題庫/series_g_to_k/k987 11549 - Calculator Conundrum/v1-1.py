# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11549 Calculator Conundrum
# ZeroJudge k987


def main():
    for _ in range(int(input())):
        print(max_num(*map(int, input().split())))


def max_num(n: int, k: int) -> int:
    nums = set()
    limit = 10 ** n
    while k not in nums:
        if k == limit - 1:
            return k
        nums.add(k)
        k **= 2
        while k >= limit:
            k //= 10
    return max(nums)


main()
