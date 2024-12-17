# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a233
# 
# 使用 python 內建的 sort (TimSort)


def main():
    n = int(input())
    nums = input().split()
    nums.sort(key=int)
    print(*nums)


main()
