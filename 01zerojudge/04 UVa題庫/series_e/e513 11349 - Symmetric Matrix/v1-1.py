# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11349 Symmetric Matrix
# ZeroJudge e513

for case in range(1, int(input()) + 1):
    n = int(input().split()[-1])
    matrix = [[int(i) for i in input().split()] for _ in range(n)]  # 用二維陣列紀錄
    matrix = [i for row in matrix for i in row]                     # 將二維陣列調整成一維陣列
    
    # 1. 用 any() 檢驗所有值是否都大於 0，若出現任何一個小於 0 的數，就直接輸出 Non_symmetric
    # 2. 檢驗陣列反轉後的值是否相等
    print(f'Test #{case}: {"Symmetric" if (not any(map(lambda x: x < 0, matrix))) and (matrix == matrix[::-1]) else "Non-symmetric"}.')
