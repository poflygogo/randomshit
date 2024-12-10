# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10800 Not That Kind of Graph
# ZeroJudge e633


graph = {'R': '/', 'F': '\\', 'C': '_'}
for cases in range(1, int(input()) + 1):
    trend = input().rstrip()
    total_x = len(trend)

    # 紀錄 y 的變化
    trend_value = [0]
    for i in range(1, total_x):
        if trend[i - 1] == 'R' and trend[i] != 'F':
            trend_value.append(trend_value[-1] + 1)
        elif trend[i - 1] == trend[i] == 'F' or \
            trend[i - 1] == 'C' and trend[i] == 'F':
            trend_value.append(trend_value[-1] - 1)
        else:
            trend_value.append(trend_value[-1])
    
    # 確保所有值都高於 x 軸
    min_value = min(trend_value)
    if min_value < 0:
        for i in range(len(trend_value)):
            trend_value[i] -= min_value 

    # 輸出結果
    max_value = max(trend_value)
    print(f'Case #{cases}:')
    for value in range(max_value, -1, -1):
        print('| ' + ''.join(' ' if trend_value[i] != value else graph[trend[i]] for i in range(total_x)).rstrip())
    print('+' + '-' * (total_x + 2), end='\n\n')
