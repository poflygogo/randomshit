# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f072. 3. 家裡的後花園 (Garden)
# TOI 2020-05 練習賽 新手組


if input().rstrip() == '1':
    input()
    print('0')
    exit()

garden = tuple(map(int, input().strip(' 09').split()))
if len(garden) == 1:
    print('0')
    exit()

count = 0
for idx in range(1, len(garden) - 1):
    if garden[idx] == 0 and 9 not in (garden[idx - 1], garden[idx + 1]):
        count += 1

print(count)
