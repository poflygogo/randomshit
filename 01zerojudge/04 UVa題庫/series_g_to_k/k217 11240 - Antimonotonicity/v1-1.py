# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11240 Antimonotonicity
# ZeroJudge k217


for _ in range(int(input())):
    n, *arr = map(int, input().split())
    cnt = 1         # 不管怎樣都至少有 1
    flag = True     # true 代表當前應該讓數值變大, false 代表應該變小

    for i in range(1, n):
        if flag:
            if arr[i - 1] > arr[i]:
                cnt += 1
                flag ^= True
        else:
            if arr[i - 1] < arr[i]:
                cnt += 1
                flag ^= True
    print(cnt)    
