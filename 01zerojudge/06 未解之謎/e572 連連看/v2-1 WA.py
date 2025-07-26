# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e572. 連連看


from collections import defaultdict
from bisect import bisect_left


def connection(n: int, arr1: list, arr2: list):
    # 實作 LIS 最長遞增子數列問題
    find_idx = defaultdict(list)
    for i in range(n):
        find_idx[arr2[i]].append(i)
    
    arr3 = []
    for i in range(n):
        arr3.extend(find_idx.get(arr1[i], []))
    
    dp = []
    for i in arr3:
        if not dp or i > dp[-1]:
            dp.append(i)
        else:
            dp[bisect_left(dp, i)] = i
    return len(dp)


def main():
    while True:
        try:
            n = int(input())
            arr1 = input().split()
            arr2 = input().split()
            print(connection(n, arr1, arr2))
        except EOFError:
            break


main()
