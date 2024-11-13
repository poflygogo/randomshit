# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11192 Group Reverse
# ZeroJudge e267
# 
# 可參考 python 官方文檔的 itertools 的頁面最下方，找到 grouper 的函數，參考其寫法

while True:
    data = input().rstrip().split()
    group = int(data.pop(0))
    if not group:
        exit()
    
    text = data.pop()
    step = len(text) // group

    iterations = [iter(text)] * step
    result = map(lambda x: ''.join(x[::-1]), zip(*iterations))
    print(*result, sep='')
