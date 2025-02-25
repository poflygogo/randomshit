# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11854 Egypt
# ZeroJudge j037


arr = sorted(map(int, input().split()))
while any(arr):
    print('right' if arr[0] ** 2 + arr[1] ** 2 == arr[2] ** 2 else 'wrong')
    arr = sorted(map(int, input().split()))
