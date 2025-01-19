# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f339. 3.下雪的日子(Snow)
# 2020-08 TOI 新手同好會


n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(m)]
data.sort()

# 移除長度為 0 的區間
i = 0
while i < len(data):
    if data[i][0] == data[i][1]:
        del data[i]
    else:
        i += 1

# 合併區間
data_merge = [data[0]]
for i in range(1, len(data)):
    if data[i][0] <= data_merge[-1][1] < data[i][1]:
        data_merge[-1][1] = data[i][1]
    elif data[i][0] > data_merge[-1][1]:
        data_merge.append(data[i])

# 準備輸出結果
result = []
if data_merge[0][0] != 0:
    result.append([0, data_merge[0][0]])
result.extend([[data_merge[i - 1][1], data_merge[i][0]] for i in range(1, len(data_merge))])
if data_merge[-1][1] != n:
    result.append([data_merge[-1][1], n])

print('\n'.join(f'{a} {b}' for a, b in result))
