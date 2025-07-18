# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e166. 演唱會記行 - 粉絲應援


# 環形卡丹
# 同時實作最小數列和和最大數列和
n = int(input())
while n:
    arr = list(map(int, input().split()))
    result = float("-inf")
    max_curr = max_global = min_curr = min_global = arr[0]
    for i in range(1, n):
        max_curr = max(arr[i], max_curr + arr[i])
        max_global = max(max_global, max_curr)
        min_curr = min(arr[i], min_curr + arr[i])
        min_global = min(min_global, min_curr)
    
    total = sum(arr)
    if min_global == total:
        result = max_global
    else:
        result = max(max_global, total - min_global)
    print(result)
    n = int(input())
