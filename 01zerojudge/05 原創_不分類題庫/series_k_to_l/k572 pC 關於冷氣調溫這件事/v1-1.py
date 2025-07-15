# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k572. pC. 關於冷氣調溫這件事


data = [tuple(map(int, input().split())) for _ in range(int(input()))]
data.sort(key=lambda x: (x[1], x[0]), reverse=True)

result = {}
for i in range(len(data)):
    cnt = 0
    for j in range(len(data)):
        if data[j][0] <= data[i][1]:
            if data[j][1] >= data[i][1]:
                cnt += 1
            else:
                break
    result[data[i][1]] = cnt

print(max(result, key=lambda x: result[x]))
