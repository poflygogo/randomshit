# -*- encoding: utf-8 -*-
# python 3.12
# UVa 161 - Traffic Lights
# ZeroJudge q898


from sys import stdin


def traffic_light(arr: list, time_limit: int = 60 * 60 * 5):
    for sec in range(min(arr) * 2, time_limit + 1):
        if all(sec % (2 * i) < i - 5 for i in arr):
            return "{:02d}:{:02d}:{:02d}".format(sec // 3600, sec // 60 % 60, sec % 60)
    return "Signals fail to synchronise in 5 hours"


def main():
    # 輸入格式麻煩，直接用 sys.stdin 一口氣全讀進來比較好處理
    data = stdin.read().split()
    del data[-3:]
    data = [int(i) for i in data]
    length = len(data)
    prev = 0
    while True:
        idx = data.index(0, prev)
        print(traffic_light(data[prev:idx]))
        if idx == length - 1:
            break
        prev = idx + 1


main()
