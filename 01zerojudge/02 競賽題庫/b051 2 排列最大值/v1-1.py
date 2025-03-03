# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b051. 2. 排列最大值
# 96學年度高雄市資訊學科能力競賽


while True:
    try:
        n, *arr = input().split()
    except EOFError:
        break
    n = int(n)

    # bubble sort
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] < arr[j] + arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    print(''.join(arr))
