# # # -*- encoding: utf-8 -*-
# # # python 3.12
# # # ZeroJudge h082. 2. 贏家預測
# # # 2022-01 APCS


from operator import mul

n, m = map(int, input().split())
data = list(map(list,                               # [戰力, 應變力, 失敗場數, 編號]
                zip(map(int, input().split()),      # 戰力
                    map(int, input().split()),      # 應變力
                    [0] * n,                        # 失敗場數, 預設為 0
                    range(1, n + 1))))              # 編號
data = [i[1] for i in sorted(zip(map(int, input().split()), data))]

print(*data, sep='\n', end='\n\n')

while len(data) > 1:
    win, loss = [], []
    for i in range(1, len(data), 2):
        mul_a, mul_b = mul(*data[i - 1][:2]), mul(*data[i][:2]) # 戰力 * 應變力

        # 確保排序在前的始終是贏家 (i - 1 是贏家, i 是輸家)
        if mul_a < mul_b:
            data[i], data[i - 1] = data[i - 1], data[i]
            mul_a, mul_b = mul_b, mul_a
        
        a, b, c, d = *data[i - 1][:2], *data[i][:2]
        data[i - 1][0] += mul_b // (2 * b)
        data[i - 1][1] += mul_b // (2 * a)
        data[i][0] += c // 2
        data[i][1] += d // 2
        data[i][2] += 1

        win.append(data[i - 1])
        if data[i][2] < m:
            loss.append(data[i])

    if len(data) & 1:
        win.append(data[-1])
    
    data = win + loss

    print(*data, sep='\n', end='\n\n')

print(data[0][-1])
