# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge f431. 高雄市109年資訊競賽國中組第八題
# 高雄市109年資訊競賽國中組第八題


group_a = []
group_b = []
for _ in range(int(input())):
    g, s, t = map(int, input().split())
    if g == 1:
        group_a.append([s, t])
    else:
        group_b.append([s, t])


group_a.sort()
group_b.sort()


def get_interval(iterator: list):
    """把重疊的部分個別整合起來"""
    if not iterator:
        return iterator
    interval = [iterator[0]]
    for s, t in iterator[1:]:
        if s <= interval[-1][1] < t:
            interval[-1][1] = t
        elif s > interval[-1][1]:
            interval.append([s, t])
    return interval


group_a, group_b = map(get_interval, (group_a, group_b))

result = []
for a in group_a:
    for b in group_b:
        # 當 a 的開始時間比 b 的結束時間晚，跳過當前這個 b
        if a[0] > b[1]:
            continue

        # 當 a 的結束時間比 b 的開始時間早，直接紀錄起來並 break
        if a[1] < b[0]:
            result.append(a)
            break

        # 當 a 的開始時間介於 b 的開始時間與結束時間之間
        if b[0] <= a[0] <= b[1]:
            if a[1] <= b[1]:
                break
            else:
                a[0] = b[1]
        
        # 當 a 的開始時間比 b 的開始時間早
        # TODO: 目前沒頭緒怎麼拆，a 的範圍可能比 b 長，需要拆分成好幾段
        
    

    else:
        result.append(a)
