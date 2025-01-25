# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e800. p7. 影片推薦
# 2019-12 TOI 新手同好會


def recommend(data):
    data = tuple(map(int, data[1:]))
    return data[0] * data[2] * data[3] / data[1]


data = [input().split() for i in range(int(input()))]
data.sort(key=recommend, reverse=True)
print('\n'.join(i[0] for i in data))
