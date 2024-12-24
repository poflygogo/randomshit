# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c159. NOIP2014 1.珠心算测试
# NOIP 2014 普及組 第一題s


def main():
    n = int(input())
    nums = tuple(map(int, input().split()))
    nums_set = set(nums)
    print(len({nums[i] + nums[j] for i in range(n) for j in range(i + 1, n) if nums[i] + nums[j] in nums_set}))


if __name__ == '__main__':
    main()
