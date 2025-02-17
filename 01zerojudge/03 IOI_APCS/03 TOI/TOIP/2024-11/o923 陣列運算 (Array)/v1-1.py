# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge o923. 陣列運算 (Array)
# 2024-11 TOI 練習賽 新手組 第三題


def operate(target):
    if target[0] % 3 == 0:
        result = max(target)
        for i in range(5):
            if target[i] == result:
                target[i] //= 2
    else:
        result = min(i for i in target if i != 0)
        for i in range(5):
            if target[i] == result:
                target[i] -= 1
    return result


arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

n = operate(arr1)
print(n)
while n != 0:
    if n & 1:
        n = operate(arr1)
    else:
        n = operate(arr2)
    print(n)
