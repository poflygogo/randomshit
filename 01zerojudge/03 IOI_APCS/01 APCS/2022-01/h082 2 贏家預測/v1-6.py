# # -*- encoding: utf-8 -*-
# # python 3.12
# # ZeroJudge h082. 2. 贏家預測
# # 2022-01 APCS


from operator import mul

n, m = map(int, input().split())
data = {i: [j]                                          # {id: [戰力, 應變力, 敗場]}
        for i, j in zip(range(1, n + 1),                # id
                        map(int, input().split()))}     # 戰力
for i, j in enumerate(map(int, input().split())):
    data[i + 1].extend([j, 0])                          # 應變力, 敗場
arr = list(map(int, input().split()))

while len(arr) > 1:
    win, loss = [], []
    for i in range(1, len(arr), 2):
        mul_a, mul_b = mul(*data[arr[i - 1]][:2]), mul(*data[arr[i]][:2])

        # 確保排序在前的始終是贏家
        if mul_a < mul_b:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            mul_a, mul_b = mul_b, mul_a
        
        temp = mul_b // (2 * data[arr[i - 1]][1])                  # a + cd // 2b
        data[arr[i - 1]][1] += mul_b // (2 * data[arr[i - 1]][0])  # b + cd // 2a
        data[arr[i - 1]][0] += temp
        data[arr[i]][0] += data[arr[i]][0] // 2                    # c + c // 2
        data[arr[i]][1] += data[arr[i]][1] // 2                    # d + d // 2
        data[arr[i]][2] += 1                                       # 失敗場數加 1

        win.append(arr[i - 1])
        if data[arr[i]][2] < m:
            loss.append(arr[i])
        
    if len(arr) & 1:
        win.append(arr[-1])
    
    arr = win + loss

print(arr[0])
