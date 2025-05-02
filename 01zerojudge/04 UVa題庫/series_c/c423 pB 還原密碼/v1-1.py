# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c423. pB 還原密碼
# 104學年度全國資訊學科能力競賽


n, r = map(int, input().split())
num = list(input())

# find possible digit to insert
temp_sum = sum(map(int, num))
possible = []
for i in range(10):
    temp = temp_sum + i
    while temp >= 10:
        temp = sum(map(int, str(temp)))
    if temp == r:
        possible.append(str(i))

# list all possible answer and ignore duplicate
result = set()
for i in possible:
    num.insert(0, i)
    result.add(''.join(num))
    for i in range(n - 1):
        num[i], num[i + 1] = num[i + 1], num[i]
        result.add(''.join(num))
    num.pop()

# sort, remove the max and the minimum value
result = sorted(result)
result.pop()
result.pop(0)

print('\n'.join(result))
