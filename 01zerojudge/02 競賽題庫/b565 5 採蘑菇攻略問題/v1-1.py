# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b565. 5.採蘑菇攻略問題


while True:
    try:
        n, *nums = map(int, input().split())
    except EOFError:
        break

    # Kadane's Algorithm
    result = temp = 0
    for i in nums:
        temp = max(i, temp + i)
        result = max(result, temp)
    print(result)
