# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11078 Open Credit System
# ZeroJudge i959


for _ in range(int(input())):
    n = int(input())
    arr = tuple(map(int, input().split()))
    result = float('-inf')
    max_value = arr[0]

    for i in range(1, n):
        result = max(result, max_value - arr[i])
        max_value = max(max_value, arr[i])
    
    print(result)
