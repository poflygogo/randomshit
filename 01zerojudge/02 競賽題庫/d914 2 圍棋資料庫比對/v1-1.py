# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d914. 2. 圍棋資料庫比對
# 99學年度全國資訊學科能力競賽

def reader():
    n = int(input())
    record = {}
    for _ in range(n):
        x, y, color = map(int, input().split())
        record[(x, y)] = color
    return record

record1 = reader()
record2 = reader()
difference = set(record1).symmetric_difference(set(record2))
intersection = set(record1).intersection(set(record2))

print(len(difference) + 2 * sum(record1[i] != record2[i] for i in intersection))
