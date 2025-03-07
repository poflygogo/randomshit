# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a046. 迴圈中斷練習


while True:
    try:
        n = int(input())
    except EOFError:
        break

    result = sum(i for i in range(1, n + 1) if i % 3 and i % 5)

    if result >= 2008:
        print('overflow')
        # break     # 題目騙人，不用 break
    else:
        print(result)
