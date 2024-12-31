# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f250. ugly ++


def geometric_sequence_generator(start=1, stop=10**18, sep=1, pre=1):
    # 等比數列生成器
    n = start
    while n * pre <= stop:
        yield n
        n *= sep


ugly_nums = [
    i * j * k
    for i in geometric_sequence_generator(sep=2)
    for j in geometric_sequence_generator(sep=3, pre=i)
    for k in geometric_sequence_generator(sep=5, pre=i * j)
]
ugly_nums.sort()
for _ in range(int(input())):
    print(ugly_nums[int(input()) - 1])
