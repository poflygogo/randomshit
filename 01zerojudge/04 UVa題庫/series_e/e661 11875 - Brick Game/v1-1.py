# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11875 Brick Game
# Zerojudge e661


for cases in range(1, int(input()) + 1):
    arr = input().split()
    print('Case', f'{cases}:', arr[int(arr[0]) // 2 + 1])
