# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge n137. p9. 報表排序
# 110新北市資訊學科能力複賽

for _ in range(int(input())):
    data = list(zip(input().split(), input().split()))
    data.sort(key=lambda x: (x[0], int(x[1])))
    print('\n'.join(' '.join(i) for i in data))
