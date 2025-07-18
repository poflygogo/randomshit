# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e166. 演唱會記行 - 粉絲應援


# 硬爆 n 次卡丹算法
# 時間複雜度 O(n^2)

n = int(input())
while n:
    arr = list(map(int, input().split()))
    result = float("-inf")
    for i in range(len(arr)):
        j = (i + 1) % n
        max_curr = max_global = arr[i]
        while j != i:
            max_curr = max(arr[j], max_curr + arr[j])
            max_global = max(max_curr, max_global)
            j = (j + 1) % n
        result = max(result, max_global)
    print(result)
    n = int(input())
