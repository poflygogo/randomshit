# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f819. 圖書館 (Library)
# 2021-04 TOI 練習賽 新手組


books = tuple(filter(lambda x: x[1] > 100, [tuple(map(int, input().split())) for _ in range(int(input()))]))
if not books:
    print('0')
else:
    print(*sorted(i for i, _ in books))
    print(sum(5 * (i - 100) for _, i in books))
