# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d784. 一、連續元素的和


def max_sub_array(length: int, nums: list) -> int:
    return max(sum(nums[i:j]) for i in range(length) for j in range(i + 1, length + 1))


def main():
    for _ in range(int(input())):
        n, *nums = map(int, input().split())
        print(max_sub_array(n, nums))


main()
