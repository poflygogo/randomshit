# -*- encoding: utf-8 -*-
# python 3.12
# UVa 01260 Sales
# ZeroJudge i855


for _ in range(int(input())):
    n = int(input())
    arr = tuple(map(int, input().split()))
    print(sum(sum(arr[j] <= arr[i] for j in range(i)) for i in range(1, n)))
