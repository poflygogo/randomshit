# -*- encoding: utf-8 -*-
# python 3.12


def my_combinations(args, max_length, comb, start=0):
    """
    *args:
        args: 要排列組合的元素
        depth: 要取出多少元素進行排列組合
        comb : 紀錄目前可能的答案
        start: 紀錄目前走到哪個 index
    """
    if len(comb) == max_length:
        print(comb)
        return
    for i in range(start, len(args)):
        comb.append(args[i])
        my_combinations(args, max_length=max_length, comb=comb, start=i + 1)
        comb.pop()


if __name__ == '__main__':
    my_combinations([1, 2, 3, 4], max_length=3, comb=[])
