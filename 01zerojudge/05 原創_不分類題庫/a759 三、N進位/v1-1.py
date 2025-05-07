# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a759. 三、N進位
# 102學年度板橋高中校內資訊學科能力競賽


a = int(input())
result = []
for _ in range(int(input())):
    base, num = input().split()
    num = int(num, int(base))
    if num >= a:
        continue
    num += a
    s = sum(i == '1' for i in bin(num)[2:])
    result.append(s)
print(max(result), result.count(max(result)))
