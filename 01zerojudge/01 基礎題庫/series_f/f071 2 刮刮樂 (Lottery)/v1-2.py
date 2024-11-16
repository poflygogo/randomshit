# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f071. 2. 刮刮樂 (Lottery)
# TOI 2020-05 練習賽 新手組


num_lucky = tuple(map(int, input().split()))
num_lottery = tuple(zip(map(int, input().split()), map(int, input().split())))
key = {}
for i, j in num_lottery:
    if i not in key:
        key[i] = j
    else:
        key[i] += j

result = 0
if num_lucky[0] in key:
    result += key[num_lucky[0]]

if num_lucky[1] in key:
    result += key[num_lucky[1]]

if num_lucky[2] in key:
    result -= key[num_lucky[2]]
else:
    result *= 2

print('0' if result < 0 else result)
