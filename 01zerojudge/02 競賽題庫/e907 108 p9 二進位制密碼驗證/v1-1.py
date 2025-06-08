# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e907. 108 p9. 二進位制密碼驗證
# 108新北市資訊學科能力複賽


pwd = input().rstrip()

result = []
if any(i not in '10' for i in pwd):
    result.append(1)

if not 8 <= len(pwd) <= 12:
    result.append(2)

counter = {'0': 0, '1': 0}
for i in pwd:
    if i in counter:
        counter[i] += 1
    if counter['0'] >= 2 and counter['1'] >= 3:
        break

if counter['0'] < 2:
    result.append(3)

if counter['1'] < 3:
    result.append(4)

if '101' not in pwd:
    result.append(5)

if result:
    print(*result)
else:
    print(0)
