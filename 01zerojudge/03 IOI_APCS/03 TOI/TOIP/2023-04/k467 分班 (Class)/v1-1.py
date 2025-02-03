# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k467. 分班 (Class)
# 2023-04 TOI 練習賽 新手組


input() # len(chinese), 用不到的資訊
chinese = map(int, input().split())
math = map(int, input().split())

result = [[], []]
for i, j in enumerate(zip(chinese, math)):
    result[j[0] < j[1]].append(str(i + 1))

print('\n'.join(' '.join(i) if i else '-1' for i in result))
