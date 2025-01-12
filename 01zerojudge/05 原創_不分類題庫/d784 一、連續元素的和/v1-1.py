# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d784. 一、連續元素的和

# Kadane's Algorithm
# https://quanticdev.com/algorithms/dynamic-programming/kadanes-algorithm/


def max_sub_array(length: int, nums: list) -> int:
    # Kadane's Algorithm
    max_curr = max_global = nums[0]
    for i in range(1, length):
        max_curr = max(nums[i], max_curr + nums[i])
        max_global = max(max_curr, max_global)
    return max_global


def main():
    for _ in range(int(input())):
        n, *nums = map(int, input().split())
        print(max_sub_array(n, nums))


main()
