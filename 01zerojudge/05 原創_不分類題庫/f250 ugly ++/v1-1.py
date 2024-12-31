# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f250. ugly ++


def geometric_sequence_generator(start=1, stop=10**18, step=1, pre=1):
    """
    返回一個生成器，用於生成一個等比數列。
    args:
        start: int, 從這個數字開始生成, 預設為 1。
        stop : int, 生成的數字的最大值, 預設為 10**18。
        step : int, 等差數列的公比, 預設為 1。
        pre  : int, 這題目的特供版參數, 用於避免無謂的運算。
    yield:
        int
    """
    n = start
    while n * pre <= stop:
        yield n
        n *= step


ugly_nums = [
    i * j * k
    for i in geometric_sequence_generator(step=2)
    for j in geometric_sequence_generator(step=3, pre=i)
    for k in geometric_sequence_generator(step=5, pre=i * j)
]
ugly_nums.sort()
for _ in range(int(input())):
    print(ugly_nums[int(input()) - 1])
