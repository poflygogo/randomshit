# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11942 Lumberjack Sequencing
# ZeroJudge e533


print('Lumberjacks:')
for _ in range(int(input())):
    arr = tuple(map(int, input().split()))
    if all(arr[i] < arr[i + 1] for i in range(9)) or all(arr[i] > arr[i + 1] for i in range(9)):
        print('Ordered')
    else:
        print('Unordered')
