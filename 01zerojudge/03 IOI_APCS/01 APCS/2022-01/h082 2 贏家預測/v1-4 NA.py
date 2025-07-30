# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge h082. 2. 贏家預測
# 2022-01 APCS


n, m = map(int, input().split())
power = list(map(int, input().split()))
response = list(map(int, input().split()))
arr = list(map(lambda x: int(x) - 1, input().split()))
loss_cnt = [0] * n

while len(arr) > 1:
    win, loss = [], []
    for i in range(1, len(arr), 2):
        mul_a, mul_b = power[arr[i - 1]] * response[arr[i - 1]], power[arr[i]] * response[arr[i]]

        if mul_a < mul_b:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            mul_a, mul_b = mul_b, mul_a
        
        power[arr[i - 1]] += mul_b // (2 * response[arr[i - 1]])
        response[arr[i - 1]] += mul_b // (2 * power[arr[i - 1]])
        power[arr[i]] += power[arr[i]] // 2
        response[arr[i]] += response[arr[i]] // 2
        loss_cnt[arr[i]] += 1

        win.append(arr[i - 1])
        if loss_cnt[arr[i]] < m:
            loss.append(arr[i])
        
    if len(arr) & 1:
        win.append(arr[-1])
    arr = win + loss

print(arr[0] + 1)
